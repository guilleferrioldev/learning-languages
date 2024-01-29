package main

import "fmt"

func main() {
	// Array
	var intArr3 [3]int32
	intArr3[1] = 123

	var pointerIntArr3 = &intArr3[1]

	fmt.Println(pointerIntArr3)

	var sliceIntArr3 = intArr3[0:2]

	fmt.Println(sliceIntArr3)

	intArr4 := [...]int32{1, 2, 3, 4}
	intArr5 := [5]int32{1, 2, 3, 4, 5}

	fmt.Println(intArr4)

	var appendIntArr []int32 = []int32{4, 5, 6}
	appendIntArr = append(appendIntArr, 7)
	fmt.Println(appendIntArr)

	var length int = len(appendIntArr)
	var capacity int = cap(appendIntArr)

	fmt.Printf("Length %v Capacity %v \n", length, capacity)

	var intSlice3 []int32 = make([]int32, 3, 8)
	fmt.Println(intSlice3)

	// Map
	var myMap map[string]uint8 = make(map[string]uint8)
	fmt.Println(myMap)

	var myMap2 = map[string]uint8{"Adam": 32, "Sarah": 25}
	myMap2["Alex"] = 40
	fmt.Println(myMap2)

	var age, ok = myMap2["Jason"]
	if ok {
		fmt.Println(age)
	} else {
		fmt.Println("Invalid Name")
	}

	for i := 0; i < 10; i += 2 {
		fmt.Println(i)
	}

	for index, value := range intArr5 {
		fmt.Printf("Index %v, Value %v \n", index, value)
	}

	for name, age := range myMap2 {
		fmt.Printf("%v : %v \n", name, age)
	}
}
