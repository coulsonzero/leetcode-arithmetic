var majorityElement = function(nums) {
    let map = new Map()
    for (let num of nums) {
        map[num] = (map[num] || 0) + 1
    }
    let ans = []
    for (let key in map) {
        if (map[key] > nums.length / 3) {
            ans.push(key)
        }
    }
    return ans
};