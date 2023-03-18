# Valid Palindrome with Removal


## Question

This question is asked by Facebook. Given a string and the ability to delete at most one character, return whether or not it can form a palindrome.

Note: a palindrome is a sequence of characters that reads the same forwards and backwards.

Ex: Given the following strings...

```
"abcba", return true
"foobof", return true (remove the first 'o', the second 'o', or 'b')
"abccab", return false
```

## Solution

<details>
  <summary>Show solution</summary>

```python
def valid_palindrome_with_removal(text: str) -> bool:
    if text == text[::-1]:
        return True
    for i in range(len(text)):
        if text[:i] + text[i+1:] == text[i+1:][::-1] + text[:i][::-1]:
            return True
    return False
```

</details>
