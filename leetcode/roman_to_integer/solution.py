def roman_to_int(s: str) -> int:
    values_add = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    values_sub = {
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900
    }

    result = 0

    for val in values_sub:
        if val in s:
            result += values_sub[val]
            s = s.replace(val, '')

    for char in s:
        result += values_add[char]

    return result
