# Valid Palindrome

## Question

This question is asked by Facebook. Given a string, return whether or not it forms a palindrome ignoring case and non-alphabetical characters.

Note: a palindrome is a sequence of characters that reads the same forwards and backwards.

Ex: Given the following strings...

```
"level", return true
"algorithm", return false
"A man, a plan, a canal: Panama.", return true
```

## Solution

<details>
  <summary>Show solution</summary>

```python
def valid_palindrome(text: str):
    alphabetical_text = ''.join(character.lower() for character in text if character.isalpha())
    return alphabetical_text == alphabetical_text[::-1]
```

</details>
