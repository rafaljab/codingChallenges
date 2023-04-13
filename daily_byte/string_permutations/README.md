# String Permutations

## Question

This question is asked by Amazon. 
Given a string `s` consisting of only letters and digits, where we are allowed to transform any letter to uppercase or lowercase, return a list containing all possible permutations of the string.

Ex: Given the following string…

```
S = "c7w2", return ["c7w2", "c7W2", "C7w2", "C7W2"]
```

## Solution

<details>
  <summary>Show solution</summary>

```python
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
```

</details>
