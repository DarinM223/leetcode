def longestConsecutive(nums: list[int]) -> int:
    if not nums:
        return 0

    nums_set = set(nums)
    max_consecutive = 0
    for num in nums:
        if num - 1 not in nums_set:
            count = 0
            while num in nums_set:
                num += 1
                count += 1
            max_consecutive = max(max_consecutive, count)
    return max_consecutive


longestConsecutive([])
longestConsecutive([100, 4, 200, 1, 3, 2])
longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
longestConsecutive([1, 0, 1, 2])
