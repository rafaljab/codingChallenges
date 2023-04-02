# Intersection of Numbers

## Question

This question is asked by Google. 
Given two integer arrays, return their intersection.

Note: the intersection is the set of elements that are common to both arrays.

Ex: Given the following arrays...

```
nums1 = [2, 4, 4, 2], nums2 = [2, 4], return [2, 4]
nums1 = [1, 2, 3, 3], nums2 = [3, 3], return [3]
nums1 = [2, 4, 6, 8], nums2 = [1, 3, 5, 7], return []
```

## Solution

<details>
  <summary>Show solution</summary>

Solution 1
```python
def intersection_of_numbers(nums1: list[int], nums2: list[int]) -> list[int]:
    return list(set(nums1) & set(nums2))
```

Solution 2
```python
def intersection_of_numbers_2(nums1: list[int], nums2: list[int]) -> list[int]:
    results = []
    for num1 in nums1:
        if num1 in nums2 and num1 not in results:
            results.append(num1)
    return results
```

</details>
