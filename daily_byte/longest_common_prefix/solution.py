def longest_common_prefix(data: list[str]) -> str:
    data.sort(key=lambda x: len(x))
    result = ''
    for i, char in enumerate(data[0]):
        for word in data[1:]:
            if word[i] != char:
                return result
        result += char
    return result
