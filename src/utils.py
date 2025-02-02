def upper_alpha(s: str) -> str:
    return "".join(filter(lambda x: x.isalpha(), s)).upper()
