def intersection_of_numbers(nums1: list[int], nums2: list[int]) -> list[int]:
    return list(set(nums1) & set(nums2))


def intersection_of_numbers_2(nums1: list[int], nums2: list[int]) -> list[int]:
    results = []
    for num1 in nums1:
        if num1 in nums2 and num1 not in results:
            results.append(num1)
    return results
