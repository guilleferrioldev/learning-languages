package main

import (
	"errors"
	"fmt"
)

func printFunc(fn func(int16, int16) (int16, int16, error), a int16, b int16) {
	result, remainder, err := fn(a, b)
	if err != nil {
		fmt.Println(err.Error())
	} else {
		fmt.Printf("Result %v remainder %v \n", result, remainder)
	}
}

func intDivision(numerator int16, denominator int16) (int16, int16, error) {
	var err error
	if denominator == 0 {
		err = errors.New("Cannot Divide by Zero")
		return 0, 0, err
	}

	var result int16 = numerator / denominator
	var remainder int16 = numerator % denominator
	return result, remainder, err

}

func intSum(operator1 int, operator2 int) int {
	return operator1 + operator2
}

func main() {
	printFunc(intDivision, 4, 3)

	var firstClassSumFunc func(int, int) int
	firstClassSumFunc = intSum
	result := firstClassSumFunc(4, 3)
	fmt.Println(result)
}
