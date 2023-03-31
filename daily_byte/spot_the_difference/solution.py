def spot_the_difference(s: str, t: str) -> str:
    diff = set(t) - set(s)
    if len(diff) > 0:
        return diff.pop()
    else:
        return ''


def spot_the_difference_2(s: str, t: str) -> str:
    for letter in t:
        if letter not in s:
            return letter
    return ''
