def add_binary(a: str, b: str) -> str:
    if len(a) > len(b):
        b = b.zfill(len(a))
    else:
        a = a.zfill(len(b))

    result = ''
    rest = 0
    for i, j in zip(a[::-1], b[::-1]):
        digit = int(i) + int(j) + rest
        if digit == 3:
            digit = 1
            rest = 1
        elif digit == 2:
            digit = 0
            rest = 1
        else:
            rest = 0
        result += str(digit)
    if rest == 1:
        result += '1'
    return result[::-1]
