package main

import (
	"fmt"
	"sync"
	"time"
)

func DoWork(idx int) {
	time.Sleep(time.Second * 3)
	fmt.Printf("[Goroutine %d]\n", idx)
}

func WithWaitGroups() {
	startTime := time.Now()
	var wg sync.WaitGroup

	for i := 0; i < 10; i++ {
		wg.Add(1)
		go func(idx int) {
			defer wg.Done()
			DoWork(idx)
		}(i)
	}
	wg.Wait()
	endTime := time.Now()
	fmt.Printf("[WaitGroups] all goroutines finished in %v seconds.\n", endTime.Second()-startTime.Second())
}

func WithoutWaitGroups() {
	startTime := time.Now()
	for i := 0; i < 10; i++ {
		go DoWork(i)
	}
	endTime := time.Now()
	fmt.Printf("[WithoutWaitGroups] finish in %v but goroutines has not been executed.\n", endTime.Second()-startTime.Second())
}

func main() {
	WithWaitGroups()
}
