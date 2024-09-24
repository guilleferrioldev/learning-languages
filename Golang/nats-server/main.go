package main

import (
	"errors"
	"log"
	"time"

	"github.com/nats-io/nats-server/v2/server"
	"github.com/nats-io/nats.go"
)

func main() {
	nc, ns, err := RunEmbeddedServer(false, true)
	if err != nil {
		log.Fatal(err)
	}

	nc.Subscribe("Hello.World", func(m *nats.Msg) {
		m.Respond([]byte("Hello there"))
	})

	ns.WaitForShutdown()
}

func RunEmbeddedServer(inProcess bool, enableLogging bool) (*nats.Conn, *server.Server, error) {
	opts := &server.Options{
		DontListen: inProcess,
	}

	ns, err := server.NewServer(opts)
	if err != nil {
		return nil, nil, err
	}

	if enableLogging {
		ns.ConfigureLogger()
	}

	go ns.Start()

	cientOpts := []nats.Option{}
	if inProcess {
		cientOpts = append(cientOpts, nats.InProcessServer(ns))
	}

	if !ns.ReadyForConnections(5 * time.Second) {
		return nil, nil, errors.New("NATS Server timeout")
	}

	nc, err := nats.Connect(ns.ClientURL(), cientOpts...)
	if err != nil {
		return nil, nil, err
	}

	return nc, ns, nil
}
