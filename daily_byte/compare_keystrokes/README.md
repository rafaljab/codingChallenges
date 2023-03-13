# Compare Keystrokes

## Question

This question is asked by Amazon. 
Given two strings `s` and `t`, which represents a sequence of keystrokes, where `#` denotes a backspace, return whether or not the sequences produce the same result.

Ex: Given the following strings...

```
s = "ABC#", t = "CD##AB", return true
s = "como#pur#ter", t = "computer", return true
s = "cof#dim#ng", t = "code", return false
```

## Solution

<details>
  <summary>Show solution</summary>

```python
def compare_keystrokes(s: str, t: str):
    s_new = ''
    for keystroke in s:
        if keystroke == '#':
            s_new = s_new[:-1]
        else:
            s_new += keystroke

    t_new = ''
    for keystroke in t:
        if keystroke == '#':
            t_new = t_new[:-1]
        else:
            t_new += keystroke

    return s_new == t_new
```

</details>
