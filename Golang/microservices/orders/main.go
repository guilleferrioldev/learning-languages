package main

import (
	common "commons"
	"context"
	"log"
	"net"

	"google.golang.org/grpc"
)

var (
	grpcAddr = common.EnvString("GRPC_ADDR", "localhost:2000")
)

func main() {
	grpcServer := grpc.NewServer()

	l, err := net.Listen("tcp", grpcAddr)
	if err != nil {
		log.Fatalf("failed to listen: %v", err.Error())
	}
	defer l.Close()

	store := NewStore()
	svc := NewService(store)
	NewGrpcHandler(grpcServer, svc)

	svc.CreateOrder(context.Background())

	log.Println("GRPC Server started at", grpcAddr)

	if err := grpcServer.Serve(l); err != nil {
		log.Fatalf("failed to serve: %v", err.Error())
	}
}
