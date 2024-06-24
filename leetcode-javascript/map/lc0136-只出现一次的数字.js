var singleNumber = function(nums) {
    let map = {};

    for (let num of nums) {
        map[num] = (map[num] || 0) + 1;
    }

    for (let key in map) {
        if (map[key] === 1) return key;
    }
};

var singleNumber = function(nums) {
    return nums.reduce((a,b) => a ^ b)
};