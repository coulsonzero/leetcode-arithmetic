/**
 * 多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
 * 输入：nums = [2,2,1,1,1,2,2]
 * 输出：2
 */

var majorityElement = function(nums) {
    let map = {}
    for (let num of nums) {
        map[num] = (map[num] || 0) + 1
    }
    for (key in map) {
        if (map[key] > nums.length / 2) {
            return key
        }
    }
    return -1
};