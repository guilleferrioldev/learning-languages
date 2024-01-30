package main

import (
	"crypto/sha256"
	"encoding/hex"
	"fmt"
	"math/rand"
	"sync"
	"time"
)

func ProducerInt(ch chan int) {
	for {
		ch <- rand.Intn(100)
		time.Sleep(time.Second * 3)
	}
}

func ProducerFloat(ch chan float64) {
	for {
		ch <- rand.Float64() * 100
		time.Sleep(time.Second * 3)
	}
}

func ProducerString(ch chan string) {
	for {
		bytes := []byte(fmt.Sprintf("%d", rand.Intn(100)))
		hash := sha256.Sum256(bytes)
		hashStr := hex.EncodeToString(hash[:])
		ch <- hashStr
		time.Sleep(time.Second * 3)
	}
}

func ExecuteProducers(
	chInt chan int,
	chFloat chan float64,
	chStr chan string,
) {
	var wg sync.WaitGroup

	wg.Add(3)

	go func(ch chan int) {
		defer wg.Done()
		ProducerInt(ch)
	}(chInt)

	go func(ch chan float64) {
		defer wg.Done()
		ProducerFloat(ch)
	}(chFloat)

	go func(ch chan string) {
		defer wg.Done()
		ProducerString(ch)
	}(chStr)

	wg.Wait()
}

func PrintInt(n int) {
	fmt.Printf("[PrintInt] Read %d\n", n)
}

func PrintFloat(n float64) {
	fmt.Printf("[PrintFloat] Read %.2f\n", n)
}

func PrintString(n string) {
	fmt.Printf("[PrintString] Read %s\n", n)
}

func ExecuteConsumers(
	chInt chan int,
	chFloat chan float64,
	chStr chan string,
) {
	for {
		select {
		case data := <-chInt:
			PrintInt(data)
		case data := <-chFloat:
			PrintFloat(data)
		case data := <-chStr:
			PrintString(data)
		}
	}
}

func selectChannel() {
	chInt := make(chan int)
	chFloat := make(chan float64)
	chStr := make(chan string)

	var wg sync.WaitGroup

	wg.Add(2)

	go func() {
		defer wg.Done()
		ExecuteProducers(chInt, chFloat, chStr)
	}()

	go func() {
		defer wg.Done()
		ExecuteConsumers(chInt, chFloat, chStr)
	}()

	wg.Wait()
}

func main() {
	selectChannel()
}
