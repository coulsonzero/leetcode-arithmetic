var twoSum = function(nums, target) {
    let m = new Map()
    for(let i = 0; i < nums.length; i++) {
        x = target - nums[i]
        if(m.has(x)) {
            return [m.get(x), i]
        }
        m.set(nums[i], i)
    }
    return [-1, -1]
};


var twoSum = function(nums, target) {
    let m = new Map()
    for(let i = 0; i < nums.length; i++) {
        x = target - nums[i]
        if(m[x] != undefined) {
            return [m[x], i]
        }
        m[nums[i]] = i
    }
    return [-1, -1]
};