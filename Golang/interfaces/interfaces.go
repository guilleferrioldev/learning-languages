package main

import "fmt"

type engine interface {
	milesLeft() uint8
	missingLitersTank() uint8
}

type gasEngine struct {
	mpg       uint8
	gallons   uint8
	fullTank  uint8
	ownerInfo owner
}

func (e gasEngine) milesLeft() uint8 {
	return e.gallons * e.mpg
}

func (e gasEngine) missingLitersTank() uint8 {
	return e.fullTank - e.gallons
}

type owner struct {
	name string
}

var myEngine2 = struct {
	mpg     uint8
	gallons uint8
}{10, 5}

func main() {
	var myEngine = gasEngine{25, 15, 40, owner{"Alex"}}
	myEngine.mpg = 20

	fmt.Println(myEngine.mpg, myEngine.gallons, myEngine.ownerInfo.name)

	fmt.Printf("Missing liters in the tank %v\n", myEngine.missingLitersTank())
	fmt.Printf("Total miles left in tank %v\n", myEngine.milesLeft())

	fmt.Println(myEngine2.mpg, myEngine2.gallons)
}
