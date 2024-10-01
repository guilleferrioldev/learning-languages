package main

import (
	pb "commons/api"
	"context"
	"log"

	"google.golang.org/grpc"
)

type grpcHandler struct {
	pb.UnimplementedOrdersServiceServer

	service *service
}

func NewGrpcHandler(grpcServer *grpc.Server, service *service) {
	handler := &grpcHandler{
		service: service,
	}
	pb.RegisterOrdersServiceServer(grpcServer, handler)
}

func (h *grpcHandler) CreateOrder(ctx context.Context, req *pb.CreateOrderRequest) (*pb.Order, error) {
	log.Printf("New order received %v", req)
	o := &pb.Order{
		Id:         "123",
		CustomerId: req.CustomerId,
	}
	return o, nil
}
