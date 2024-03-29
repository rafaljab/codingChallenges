# 1. Two Sum

https://leetcode.com/problems/two-sum/

## Question

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

Example 2:
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

Example 3:
```
Input: nums = [3,3], target = 6
Output: [0,1]
```

Constraints:
* `2 <= nums.length <= 10^4`
* `-10^9 <= nums[i] <= 10^9`
* `-10^9 <= target <= 10^9`
* Only one valid answer exists.

## Solution

<details>
  <summary>Show solutions</summary>

* Brute-force:
```python
def two_sum(nums: list[int], target: int) -> list[int]:
    output = []
    for i, num1 in enumerate(nums):
        for j, num2 in enumerate(nums[i+1:]):
            if i != j + i + 1:
                if num1 + num2 == target:
                    output.append(i)
                    output.append(j + i + 1)
                    return output
```

* Using `nums.index()`:
```python
def two_sum2(nums: list[int], target: int) -> list[int]:
    for i, num in enumerate(nums):
        try:
            j = nums.index(target - num, i+1)
            return [i, j]
        except ValueError:
            pass
```

</details>
