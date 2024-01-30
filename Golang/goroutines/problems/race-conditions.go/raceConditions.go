package main

import (
	"fmt"
	"sync"
	"time"
)

var resource int
var response string
var mutex sync.Mutex

func doWork(idx int) {
	mutex.Lock()
	response += fmt.Sprintf("[Goroutine %d] Reads: %d\n", idx, resource)
	mutex.Unlock()

	resource++

	mutex.Lock()
	response += fmt.Sprintf("[Goroutine %d] Write: %d\n-----\n", idx, resource)
	mutex.Unlock()
}

func raceCondition() {
	for {
		startTime := time.Now()

		var wg sync.WaitGroup
		for i := 0; i < 10; i++ {
			wg.Add(1)
			go func(idx int) {
				defer wg.Done()
				doWork(idx)
			}(i)
		}
		wg.Wait()
		if resource == 10 {
			response = ""
			resource = 0
			continue
		} else {
			endTime := time.Now()
			fmt.Println(response)
			fmt.Printf("[RaceCondition] executed in %d seconds. Balance: %d\n", endTime.Second()-startTime.Second(), resource)
			break
		}
	}
}

func main() {
	raceCondition()
}
