package main

import "fmt"

func main() {
	var p *int32 = new(int32)
	var i int32

	fmt.Printf("The value p points to is: %v\n", *p)
	fmt.Printf("The value if i is: %v\n", i)

	p = &i
	*p = 1

	fmt.Printf("The value p points to is: %v\n", *p)
	fmt.Printf("The value if i is: %v\n", i)

	var k int32 = 2
	i = k

	fmt.Printf("The value p points to is: %v\n", *p)
	fmt.Printf("The value if i is: %v\n", i)

	var x int = 5
	var y = &x
	x += 1
	fmt.Println(x, *y)

}
