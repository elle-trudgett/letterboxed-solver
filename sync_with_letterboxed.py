# Uses Wayback Machine to grab previous Letter Boxed game data and updates dictionary file
import json
import re
import shutil

import trio
import queue
from datetime import datetime, timedelta

from typing import Any

from httpx import AsyncClient, Response

from src.dictionary import Dictionary
from src.letterbox import LetterBox

DICTIONARY_FILENAME = "words.txt"
ARCHIVE_TIMESTEP = timedelta(days=1)

dictionary: Dictionary = Dictionary.from_file(DICTIONARY_FILENAME)
print(f"Loaded {len(dictionary)} words from {DICTIONARY_FILENAME}")

archive_game_url_queue: queue.Queue = queue.Queue()
src_queue: queue.Queue = queue.Queue()
start_date: datetime = datetime.now()
seen_urls: set[str] = set()


async def get_closest(client: AsyncClient, timestamp: datetime) -> str | None:
    api_url = f"https://archive.org/wayback/available?url=https://www.nytimes.com/puzzles/letter-boxed&timestamp={timestamp.strftime('%Y%m%d%H%M%S')}"
    print(f"Looking for archived game at {timestamp.strftime('%Y-%m-%d %H:%M:%S')}.")
    api_response: Response = await client.get(api_url)
    api_response.raise_for_status()
    response_json = api_response.json()
    if "archived_snapshots" in response_json and response_json["archived_snapshots"]:
        return response_json["archived_snapshots"]["closest"]["url"]
    else:
        return None


async def fetch_archived_games() -> None:
    """Queries the archive.org API to get archived Letter Boxed game URLs and queues them for fetching."""
    date: datetime = start_date
    async with AsyncClient(timeout=10000) as client:
        while True:
            url: str | None = await get_closest(client, date)
            if url is None or url in seen_urls:
                date -= ARCHIVE_TIMESTEP
                continue
            seen_urls.add(url)
            archive_game_url_queue.put(url)
            date -= ARCHIVE_TIMESTEP


async def fetch_game_data() -> None:
    """Fetches archived Letter Boxed games and queues the HTML source for processing."""
    async with AsyncClient(timeout=10000) as client:
        while True:
            if archive_game_url_queue.empty():
                await trio.sleep(0.1)
                continue
            game_url = archive_game_url_queue.get()

            for _ in range(3):
                try:
                    print(f"Fetching game: {game_url}...")
                    response: Response = await client.get(game_url)
                    if response.status_code == 302:
                        new_location: str | None = response.headers.get("Location", None)
                        if new_location:
                            print(f"Redirected to {new_location}.")
                            if new_location not in seen_urls:
                                seen_urls.add(new_location)
                                archive_game_url_queue.put(new_location)
                            break
                    response.raise_for_status()
                    src = response.text
                    src_queue.put(src)
                    seen_urls.add(src)
                    break
                except:
                    print(f"❌ Failed to fetch game {game_url}")
                    import traceback
                    traceback.print_exc()
                    print("Waiting 10s.")
                    await trio.sleep(10)


async def sync():
    # Add today's game to the fetch queue.
    archive_game_url_queue.put("https://www.nytimes.com/puzzles/letter-boxed")

    async with trio.open_nursery() as nursery:
        nursery.start_soon(fetch_archived_games)
        nursery.start_soon(fetch_game_data)
        nursery.start_soon(processor)


async def processor():
    while True:
        if src_queue.empty():
            await trio.sleep(0.1)
            continue

        src = src_queue.get()

        match: re.Match[str] | None = re.search(r'window\.gameData = ({.*?})', src)

        if match:
            game_data_js: str = match.group(1)
            game_data: dict[str, Any] = json.loads(game_data_js)
            letterboxed_sides = game_data["sides"]
            letterboxed_dictionary = game_data["dictionary"]
        else:
            print("Did not find gameData, finishing.")
            break

        letterboxed_dictionary = set(letterboxed_dictionary)

        additions: set[str] = set()
        for word in letterboxed_dictionary:
            if word not in dictionary:
                dictionary.add(word)
                additions.add(word)

        validation_dictionary: Dictionary = dictionary.copy()
        validation_dictionary.prune(LetterBox.from_string("".join(letterboxed_sides)))

        words_to_remove: set[str] = set()

        for word in validation_dictionary.words:
            if word not in letterboxed_dictionary:
                words_to_remove.add(word)

        if len(words_to_remove) > 5000:
            print(f"Warning: aborting due to removal of {len(words_to_remove)} words")
            continue

        words_removed: set[str] = set()

        for word in dictionary.words:
            if word in words_to_remove:
                words_removed.add(word)
                dictionary.remove(word)

        if additions:
            print(f"  --> 🟢 Added {len(additions)} words to dictionary.")
        if words_to_remove:
            print(f"  --> 🔴 Removed {len(words_to_remove)} words.")

        if additions or words_to_remove:
            dictionary.save(DICTIONARY_FILENAME)
            shutil.copyfile(DICTIONARY_FILENAME, DICTIONARY_FILENAME + ".bak")
            print(f"  --> 💾 Saved {len(dictionary)} words to {DICTIONARY_FILENAME}.")
        else:
            print(f"  --> 🟡 No change ({len(dictionary)} words in dictionary.)")

        print()


if __name__ == "__main__":
    trio.run(sync)
