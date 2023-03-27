# First Unique Character

## Question

This question is asked by Microsoft. 
Given a string, return the index of its first unique character. 
If a unique character does not exist, return `-1`.

Ex: Given the following strings...

```
"abcabd", return 2
"thedailybyte", return 1
"developer", return 0
```

## Solution

<details>
  <summary>Show solution</summary>

* Solution 1
```python
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
```

* Solution 2 (Python 3.7+)
```python
def first_unique_character_2(text: str) -> int:
    chars = {}
    for i, char in enumerate(text):
        if char in chars:
            del chars[char]
        else:
            chars[char] = i
    if len(chars) == 0:
        return -1
    # dicts retaining insertion order is guaranteed for Python 3.7+
    return chars[next(iter(chars))]
```

</details>
