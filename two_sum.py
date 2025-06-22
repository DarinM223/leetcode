def twoSum(nums: list[int], target: int) -> list[int] | None:
    """
    Given an array of integers, find two numbers such that they add
    up to a specific target number

    returns an array containing i1, and i2 and i1 has to be < than
    i2. Both indexes are 1-based
    """

    # Cache the all of the numbers in the array
    cache: dict[int, int] = {}
    for i in range(0, len(nums)):
        cache[nums[i]] = i

    # Check if the expected sum - the current number is in the dictionary
    # of numbers, and the the two indexes are different
    for j in range(0, len(nums)):
        lookFor = target - nums[j]
        if lookFor in cache and cache[lookFor] != j:
            return [j + 1, cache[lookFor] + 1]

    return None
