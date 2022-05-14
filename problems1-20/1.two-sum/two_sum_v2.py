def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    hashtable = {}
    for i in range(len(nums)):
        if target - nums[i] in hashtable:
            return [i, hashtable[target - nums[i]]]
        hashtable[nums[i]] = i


nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))

        