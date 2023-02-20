# Vacuum Cleaner Route

## Question

This question is asked by Amazon. Given a string representing the sequence of moves a robot vacuum makes, return whether or not it will return to its original position. 
The string will only contain `L`, `R`, `U`, and `D` characters, representing left, right, up, and down respectively.

Ex: Given the following strings...

```
"LR", return true
"URURD", return false
"RUULLDRD", return true
```

## Solution

<details>
  <summary>Show solution</summary>

```python
def vacuum_cleaner_route(moves_sequence: str):
    horizontally = 0
    vertically = 0
    for move in moves_sequence:
        if move == 'L':
            horizontally -= 1
        if move == 'R':
            horizontally += 1
        if move == 'U':
            vertically += 1
        if move == 'D':
            vertically -= 1
    return horizontally == 0 and vertically == 0
```

</details>
