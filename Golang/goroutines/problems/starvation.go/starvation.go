package main

import (
	"fmt"
	"sync"
	"time"
)

var value int
var mutex sync.Mutex

func Goroutine() {
	mutex.Lock()
	fmt.Printf("[Goroutine] value++")
	value++
	mutex.Unlock()
}

func starvation() {
	mutex.Lock()
	go Goroutine()

	for {
		fmt.Printf("Starvation...\n")
		time.Sleep(time.Second * 3)
	}

}

func main() {
	starvation()
}
