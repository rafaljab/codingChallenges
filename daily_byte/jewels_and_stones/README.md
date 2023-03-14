# Jewels and Stones

## Question

This question is asked by Amazon.
Given a string representing your stones and another string representing a list of jewels, return the number of stones that you have that are also jewels.

Ex: Given the following jewels and stones...

```
jewels = "abc", stones = "ac", return 2
jewels = "Af", stones = "AaaddfFf", return 3
jewels = "AYOPD", stones = "ayopd", return 0
```

## Solution

<details>
  <summary>Show solution</summary>

Solution 1
```python
def jewels_and_stones(jewels: str, stones: str) -> int:
    result = 0
    for stone in stones:
        if stone in jewels:
            result += 1
    return result
```

Solution 2
```python
def jewels_and_stones(jewels: str, stones: str) -> int:
    return len([stone for stone in stones if stone in jewels])
```

</details>
