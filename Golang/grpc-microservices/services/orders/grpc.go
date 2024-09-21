package main

import (
	handler "grpc-microservices/services/orders/handler/orders"
	"grpc-microservices/services/orders/service"
	"log"
	"net"

	"google.golang.org/grpc"
)

type gRPCServer struct {
	address string
}

func NewGRPCServer(address string) *gRPCServer {
	return &gRPCServer{address: address}
}

func (server *gRPCServer) Run() error {
	listen, err := net.Listen("tcp", server.address)
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}

	grpcServer := grpc.NewServer()

	//register our grpc services
	orderService := service.NewOrderService()
	handler.NewGrpcOrdersService(grpcServer, orderService)

	log.Println("Starting gRPC server on", server.address)

	return grpcServer.Serve(listen)
}
