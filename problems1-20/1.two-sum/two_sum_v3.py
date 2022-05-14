def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    hashtable = {}
    for index, item in enumerate(nums):
        if target - item in hashtable:
            return [index, hashtable[target - item]]
        hashtable[item] = index