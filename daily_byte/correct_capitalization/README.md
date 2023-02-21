# Correct Capitalization

## Question

This question is asked by Google. Given a string, return whether or not it uses capitalization correctly. A string correctly uses capitalization if all letters are capitalized, no letters are capitalized, or only the first letter is capitalized.

Ex: Given the following strings...

```
"USA", return true
"Calvin", return true
"compUter", return false
"coding", return true
```

## Solution

<details>
  <summary>Show solution</summary>

```python
def correct_capitalization(text: str):
    return text.isupper() or text[1:].islower()
```

</details>
