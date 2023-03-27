def first_unique_character(text: str) -> int:
    chars = {}
    for i, char in enumerate(text):
        if char in chars:
            del chars[char]
        else:
            chars[char] = i
    if len(chars) == 0:
        return -1
    return sorted(chars.values())[0]


def first_unique_character_2(text: str) -> int:
    chars = {}
    for i, char in enumerate(text):
        if char in chars:
            del chars[char]
        else:
            chars[char] = i
    if len(chars) == 0:
        return -1
    return chars[next(iter(chars))]  # dicts retaining insertion order is guaranteed for Python 3.7+
