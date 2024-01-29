package main

import (
	"fmt"
	"unicode/utf8"
)

func main() {
	const num int = 10

	var intNum uint16 = 32767
	intNum = intNum + 1

	const floatNum32 float32 = 12.3
	const intNum32 int32 = 3

	const result float32 = floatNum32 + float32(intNum32)

	const myString string = "Hello" + " " + "World"

	var length int = utf8.RuneCountInString(myString)

	fmt.Println(length)

	const myRune rune = 'a'

	const myBoolen bool = false

	inferredString := "text"
	fmt.Println(inferredString)

	var1, var2 := 1, 2
	fmt.Println(var1, var2)
}
