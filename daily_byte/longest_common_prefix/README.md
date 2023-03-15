# Longest Common Prefix

## Question

This question is asked by Microsoft. 
Given an array of strings, return the longest common prefix that is shared amongst all strings.
Note: you may assume all strings only contain lowercase alphabetical characters.

Ex: Given the following arrays...

```
["colorado", "color", "cold"], return "col"
["a", "b", "c"], return ""
["spot", "spotty", "spotted"], return "spot"
```

## Solution

<details>
  <summary>Show solution</summary>

```python
def longest_common_prefix(data: list[str]) -> str:
    data.sort(key=lambda x: len(x))
    result = ''
    for i, char in enumerate(data[0]):
        for word in data[1:]:
            if word[i] != char:
                return result
        result += char
    return result
```

</details>
