# letterboxed-solver

[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
![python compatibility](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4KPCEtLSBMaWNlbnNlOiBNSVQuIE1hZGUgYnkgdnNjb2RlLWljb25zOiBodHRwczovL2dpdGh1Yi5jb20vdnNjb2RlLWljb25zL3ZzY29kZS1pY29ucyAtLT4KPHN2ZyB3aWR0aD0iODAwcHgiIGhlaWdodD0iODAwcHgiIHZpZXdCb3g9IjAgMCAzMiAzMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayI+PGRlZnM+PGxpbmVhckdyYWRpZW50IGlkPSJhIiB4MT0iLTEzMy4yNjgiIHkxPSItMjAyLjkxIiB4Mj0iLTEzMy4xOTgiIHkyPSItMjAyLjg0IiBncmFkaWVudFRyYW5zZm9ybT0idHJhbnNsYXRlKDI1MjQzLjA2MSAzODUxOS4xNykgc2NhbGUoMTg5LjM4IDE4OS44MSkiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj48c3RvcCBvZmZzZXQ9IjAiIHN0b3AtY29sb3I9IiMzODdlYjgiLz48c3RvcCBvZmZzZXQ9IjEiIHN0b3AtY29sb3I9IiMzNjY5OTQiLz48L2xpbmVhckdyYWRpZW50PjxsaW5lYXJHcmFkaWVudCBpZD0iYiIgeDE9Ii0xMzMuNTc1IiB5MT0iLTIwMy4yMDMiIHgyPSItMTMzLjQ5NSIgeTI9Ii0yMDMuMTMzIiBncmFkaWVudFRyYW5zZm9ybT0idHJhbnNsYXRlKDI1MzA5LjA2MSAzODU4My40Mikgc2NhbGUoMTg5LjM4IDE4OS44MSkiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj48c3RvcCBvZmZzZXQ9IjAiIHN0b3AtY29sb3I9IiNmZmUwNTIiLz48c3RvcCBvZmZzZXQ9IjEiIHN0b3AtY29sb3I9IiNmZmMzMzEiLz48L2xpbmVhckdyYWRpZW50PjwvZGVmcz48dGl0bGU+ZmlsZV90eXBlX3B5dGhvbjwvdGl0bGU+PHBhdGggZD0iTTE1Ljg4NSwyLjFjLTcuMSwwLTYuNjUxLDMuMDctNi42NTEsMy4wN1Y4LjM2aDYuNzUydjFINi41NDVTMiw4LjgsMiwxNi4wMDVzNC4wMTMsNi45MTIsNC4wMTMsNi45MTJIOC4zM1YxOS41NTZzLS4xMy00LjAxMywzLjktNC4wMTNoNi43NjJzMy43NzIuMDYsMy43NzItMy42NTJWNS44cy41NzItMy43MTItNi44NDItMy43MTJoMFpNMTIuMTUzLDQuMjM3YTEuMjE0LDEuMjE0LDAsMSwxLTEuMTgzLDEuMjQ0di0uMDJhMS4yMTQsMS4yMTQsMCwwLDEsMS4yMTQtMS4yMTRoMFoiIHN0eWxlPSJmaWxsOnVybCgjYSkiLz48cGF0aCBkPSJNMTYuMDg1LDI5LjkxYzcuMSwwLDYuNjUxLTMuMDgsNi42NTEtMy4wOFYyMy42NUgxNS45ODV2LTFoOS40N1MzMCwyMy4xNTgsMzAsMTUuOTk1cy00LjAxMy02LjkxMi00LjAxMy02LjkxMkgyMy42NFYxMi40cy4xMyw0LjAxMy0zLjksNC4wMTNIMTIuOTc1UzkuMiwxNi4zNTYsOS4yLDIwLjA2OFYyNi4ycy0uNTcyLDMuNzEyLDYuODQyLDMuNzEyaC4wNFptMy43MzItMi4xNDdBMS4yMTQsMS4yMTQsMCwxLDEsMjEsMjYuNTE5di4wM2ExLjIxNCwxLjIxNCwwLDAsMS0xLjIxNCwxLjIxNGguMDNaIiBzdHlsZT0iZmlsbDp1cmwoI2IpIi8+PC9zdmc+)
[![Tests](https://github.com/elle-trudgett/letterboxed-solver/actions/workflows/tests.yml/badge.svg)](https://github.com/elle-trudgett/letterboxed-solver/actions/workflows/tests.yml)

A solver for the [NYT Letter Boxed puzzle game](https://www.nytimes.com/puzzles/letter-boxed). I tried to pare down the word list to
be as similar to the list used in Letter Boxed as possible by [merging the words file](sync_with_letterboxed.py)
with previous Letter Boxed game data from the [Internet Archive Wayback Machine](https://web.archive.org/).

This is not intended to be a super-performant solver, but rather built with ❤️.

<p align="center">
  <picture align="center">
    <source media="(prefers-color-scheme: dark)" srcset="https://github.com/user-attachments/assets/e4c9eeff-0294-4f90-84dc-3681020c42dc" width="50%" max-width="968px">
    <source media="(prefers-color-scheme: light)" srcset="https://github.com/user-attachments/assets/a20ed2f1-5b35-4ad2-8aec-88277ea812db" width="50%" max-width="950px">
    <img alt="Letter Boxed solver running in interactive mode." src="https://github.com/user-attachments/assets/a20ed2f1-5b35-4ad2-8aec-88277ea812db" width="50%" max-width="950px">
  </picture>
</p>

## Quick Start

Configured with the [uv](https://github.com/astral-sh/uv) package manager.

```shell
# Run the interactive solver
make run
```

## Development

```shell
# Format and lint code
make format
make lint

# Run tests
make test

# Run all checks
make all

# Remove virtual environment
make clean
```

Requires Python 3.9+.

## TODO

1. Optimize the solver algorithm
2. Profile performance
