package main

import (
	"fmt"
	"sync"
	"time"
)

func doWork(balance *int) {
	*balance++
	time.Sleep(time.Second * 1)
}

func withoutConcurrency() {
	initTime := time.Now()
	balance := 0

	for i := 0; i < 10; i++ {
		doWork(&balance)
	}

	finishTime := time.Now()
	fmt.Printf("[WithoutConcurrency] executed in %d seconds. Balance:%d\n",
		finishTime.Second()-initTime.Second(), balance)
}

func withConcurrency() {
	initTime := time.Now()
	balance := 0

	var wg sync.WaitGroup
	for i := 0; i < 10; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			doWork(&balance)
		}()
	}
	fmt.Printf("[WithConcurrency] waiting Goroutines...\n")
	wg.Wait()

	finishTime := time.Now()
	fmt.Printf("[WithConcurrency] executed in %d seconds. Balance: %d\n",
		finishTime.Second()-initTime.Second(), balance)
}

func main() {
	withConcurrency()
}
