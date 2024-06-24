package main

/**
 * question: GP28 单词字符
 * description: 给定一个只由字母和数字组成的字符串,，统计每个字符出现的次数，并返回出现次数最多的字符
 * input : "yyds"
 * output: 'y'
 */
func character(s string) byte {
	// write code here
	charMap := make(map[byte]int)
	var count int
	var ans byte
	for _, v := range []byte(s) {
		charMap[v]++
		if charMap[v] > count {
			count = charMap[v]
			ans = v
		}
	}
	return ans
}
