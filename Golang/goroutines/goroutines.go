package main

import (
	"fmt"
	"sync"
	"time"
)

var n = sync.Mutex{}
var wg = sync.WaitGroup{}
var dbData = []string{"id1", "id2", "id3", "id4", "id5"}
var results = []string{}

func main() {
	t0 := time.Now()
	for i := 0; i < len(dbData); i++ {
		wg.Add(1)
		go dbCall(i)
	}
	wg.Wait()
	fmt.Printf("Total executuion time %v\n", time.Since(t0))
	fmt.Printf("The results are %v", results)

}

func dbCall(number int) {
	var delay float32 = 2000
	time.Sleep(time.Duration(delay) * time.Millisecond)
	fmt.Println("The result from the database is: ", dbData[number])
	n.Lock()
	results = append(results, dbData[number])
	n.Unlock()
	wg.Done()
}
