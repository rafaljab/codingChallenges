def two_sum(nums: list[int], target: int) -> list[int]:
    output = []
    for i, num1 in enumerate(nums):
        for j, num2 in enumerate(nums[i+1:]):
            if i != j + i + 1:
                if num1 + num2 == target:
                    output.append(i)
                    output.append(j + i + 1)
                    return output
