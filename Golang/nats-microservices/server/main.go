package main

import (
	"context"
	"encoding/json"
	"fmt"
	"log"
	"os"
	"os/signal"
	"syscall"

	natsServer "github.com/nats-io/nats-server/v2/server"
	"github.com/nats-io/nats.go"
)

func createServer() {

	// options to create nats server
	opts := &natsServer.Options{
		ServerName:     "local_nats_server",
		NoLog:          false,
		NoSigs:         false,
		MaxControlLine: 4096,
		MaxPayload:     65536,
	}

	// initialize the server struct
	server, err := natsServer.NewServer(opts)
	if err != nil {
		log.Fatal(err)
	}

	// run the nats server based on the options
	err = natsServer.Run(server)
	if err != nil {
		log.Fatal("Failed to start NATS server:", err)
	}

	log.Println("NATS server started")
}

type LogMessage struct {
	Message string `json:"message"`
}

func producer(ctx context.Context) {
	nc, err := nats.Connect(nats.DefaultURL)
	if err != nil {
		log.Fatal("Failed to connect to NATS server:", err)
	}
	// close the connection on function exit
	defer nc.Close()

	// listen for messages on this subject
	subject := "logs"

	i := 0

	for {
		select {
		case <-ctx.Done():
			log.Println("exiting from producer")
			return
		default:
			i += 1
			message := LogMessage{
				Message: fmt.Sprintf("%v", i),
			}

			// Encode the message to JSON
			messageJSON, err := json.Marshal(message)
			if err != nil {
				log.Println("Failed to marshal message:", err)
				continue // Skip to the next iteration
			}

			// Publish the JSON encoded message to the NATS server
			err = nc.Publish(subject, messageJSON)
			if err != nil {
				log.Println("Failed to publish message:", err)
			} else {
				log.Println(string(messageJSON)) // Log the JSON string
			}
		}
	}
}

func main() {
	ctx, cancel := context.WithCancel(context.Background())
	go func() {
		// listen for interrupts to exit gracefully
		sigChannel := make(chan os.Signal, 1)
		signal.Notify(sigChannel, os.Interrupt, syscall.SIGTERM)
		<-sigChannel
		close(sigChannel)
		cancel()
	}()

	// create the local server
	createServer()

	// register the producer
	go producer(ctx)
	<-ctx.Done()

	log.Println("server shutdown completed")
	log.Println("exiting gracefully")
}
