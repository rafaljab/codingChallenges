def spot_the_difference(s: str, t: str) -> str:
    diff = set(t) - set(s)
    if len(diff) > 0:
        return diff.pop()
    else:
        return ''
