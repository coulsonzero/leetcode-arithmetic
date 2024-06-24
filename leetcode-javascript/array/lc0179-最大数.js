/**
 * 示例
 * 输入：nums = [3,30,34,5,9]
 * 输出："9534330"
 */


var largestNumber = function(nums) {
    nums.sort((a, b) => {
        var s1 = a.toString() + b.toString()
        var s2 = b.toString() + a.toString()
        return s1 < s2 ? 1 : -1
    })
    if (nums[0] == 0) return '0'
    return nums.join('')
};