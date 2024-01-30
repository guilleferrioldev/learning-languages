package main

import "fmt"

func sumSlice[T int | float32 | float64](slice []T) T {
	var sum T

	for _, value := range slice {
		sum += value
	}
	return sum
}

func isEmpty[T any](slice []T) bool {
	return len(slice) == 0
}

func main() {
	var intSlice = []int{1, 2, 3}
	var float32Slice = []float32{1.0, 2.2, 3.3}
	var emptySlice []int

	fmt.Println(sumSlice(intSlice))
	fmt.Println(sumSlice(float32Slice))

	fmt.Println(isEmpty(intSlice))
	fmt.Println(isEmpty(emptySlice))

}
