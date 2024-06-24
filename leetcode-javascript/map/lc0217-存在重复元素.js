var containsDuplicate = function(nums) {
    nums.sort((a, b) => a - b)
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] == nums[i+1]) {
            return true
        }
    }
    return false
};

var containsDuplicate = function(nums) {
    let map = {}
    for (let num of nums) {
        map[num] = (map[num] || 0) + 1
    }
    for (let key in map) {
        if (map[key] > 1) {
            return true
        }
    }
    return false
};