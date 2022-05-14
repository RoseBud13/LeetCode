function twoSum(nums, target) {
    let hashmap = new Map();
    let result = [];
    for (let index = 0; index < nums.length; index++) {
        if (hashmap.has((target - nums[index]))) {
            result.push(index)
            result.push(hashmap.get(target - nums[index]))
            return result
        }
        hashmap.set(nums[index], index)
    }
}

n = [2,7,11,15]
t = 9
r = twoSum(n, t)
console.log(r)