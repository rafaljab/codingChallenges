import itertools


def string_permutations(s: str) -> list[str]:
    s = s.lower()

    s_dict = {}
    letter_pos = []
    for i, char in enumerate(s):
        s_dict[i] = char
        if char.isalpha():
            letter_pos.append(i)

    iters = []
    for i in range(1, len(letter_pos)+1):
        iters.append(itertools.combinations(letter_pos, i))

    results = [s, ]

    for it in iters:
        for i in it:
            s_dict_c = s_dict.copy()
            for j in i:
                s_dict_c[j] = s_dict_c[j].upper()
            ts = ''.join(s_dict_c.values())
            results.append(ts)

    return results
