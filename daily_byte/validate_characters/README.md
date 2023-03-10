# Validate Characters

## Question

This question is asked by Google. 
Given a string only containing the following characters `(`, `)`, `{`, `}`, `[`, and `]` return whether or not the opening and closing characters are in a valid order.

Ex: Given the following strings...

```
"(){}[]", return true
"(({[]}))", return true
"{(})", return false
```

## Solution

<details>
  <summary>Show solution</summary>

```python
def validate_characters(text: str):
    new_text = text
    while True:
        temp_text = new_text
        new_text = new_text.replace('()', '')
        new_text = new_text.replace('[]', '')
        new_text = new_text.replace('{}', '')

        if temp_text == new_text or new_text == '':
            return new_text == ''
```

</details>
