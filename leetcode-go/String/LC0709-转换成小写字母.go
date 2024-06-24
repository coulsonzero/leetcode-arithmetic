package main

import "strings"

/**
 * 给你一个字符串 s ，将该字符串中的大写字母转换成相同的小写字母，返回新的字符串
 * 输入：s = "Hello"
 * 输出："hello"
 * 输入：s = "here"
 * 输出："here"
 * 输入：s = "LOVELY"
 * 输出："lovely"
 */

func toLowerCase2(s string) string {
	var buf strings.Builder
	for i := 0; i < len(s); i++ {
		if 'A' <= s[i] && s[i] <= 'Z' {
			buf.WriteByte(s[i] + 32)
		} else {
			buf.WriteByte(s[i])
		}
	}


	return buf.String()
}

func toLowerCase(s string) string {
	var buf strings.Builder
	for _, c := range s {
		if 'A' <= c && c <= 'Z' {
			// buf.WriteRune(c ^ 32)
			buf.WriteRune(c + 32)
		} else {
			buf.WriteRune(c)
		}
	}
	return buf.String()
}

func main() {
	println(toLowerCase("Hello"))  		// "hello"
	println(toLowerCase("LOVELY"))  	// "lovely"
}