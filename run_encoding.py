def run_encoding(nums: list[int]) -> list[int]:
    if len(nums) == 0:
        return []

    result: list[int] = []
    curr = nums[0]
    count = 0
    for num in nums:
        if num == curr:
            count += 1
        else:
            result.append(curr)
            result.append(count)
            curr = num
            count = 1
    result.append(curr)
    result.append(count)
    return result

run_encoding([]) # []
run_encoding([8, 8, 8, 8, 5, 5, 3, 3, 3]) # [8, 4, 5, 2, 3, 3]
run_encoding([8, 8, 5, 8, 8, 8, 3, 3, 5]) # [8, 2, 5, 1, 8, 3, 3, 2, 5, 1]