package main

import (
	"fmt"
	"sync"
)

var resourceA int
var resourceB int

var mutexA sync.Mutex
var mutexB sync.Mutex

func GoroutineA() {
	mutexA.Lock()
	mutexB.Lock()

	resourceA++
	resourceB++

	mutexA.Unlock()
	mutexB.Unlock()
}

func GoroutineB() {
	mutexA.Lock()
	mutexB.Lock()

	resourceA++
	resourceB++

	mutexA.Unlock()
	mutexB.Unlock()
}

func deadLock() {
	var wg sync.WaitGroup

	wg.Add(2)

	go func() {
		defer wg.Done()
		for {
			GoroutineA()
		}
	}()

	go func() {
		defer wg.Done()
		for {
			GoroutineB()
		}
	}()

	wg.Wait()
	fmt.Printf("ResourceA: %d\n", resourceA)
	fmt.Printf("ResourceB: %d\n", resourceB)
}

func main() {
	deadLock()
}
