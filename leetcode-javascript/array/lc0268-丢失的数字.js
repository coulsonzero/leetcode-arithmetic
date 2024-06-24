var missingNumber = function(nums) {
    nums.sort((a, b) => a - b)
    let n = nums.length
    for (let i = 0; i < n; i++) {
        if (nums[i] !== i) {
            return i
        }
    }
    return n
};