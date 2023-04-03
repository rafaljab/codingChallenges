def remove_adjacent_duplicates(s: str) -> str:
    while True:
        length_of_s = len(s)
        last_char = ''
        for i, char in enumerate(s):
            if last_char == char:
                s = s[:i-1] + s[i+1:]
                break
            last_char = char
        if length_of_s == len(s):
            return s
