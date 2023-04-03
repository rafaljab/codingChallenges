# Remove Adjacent Duplicates


## Question

This question is asked by Facebook. 
Given a string `s` containing only lowercase letters, continuously remove adjacent characters that are the same and return the result.

Ex: Given the following strings...

```
s = "abccba", return ""
s = "foobar", return "fbar"
s = "abccbefggfe", return "a"
```

## Solution

<details>
  <summary>Show solution</summary>

```python
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
```

</details>
