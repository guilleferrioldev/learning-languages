package main

import (
	handler "grpc-microservices/services/orders/handler/orders"
	"grpc-microservices/services/orders/service"
	"log"
	"net/http"
)

type httpServer struct {
	addr string
}

func NewHttpServer(addr string) *httpServer {
	return &httpServer{addr: addr}
}

func (server *httpServer) Run() error {
	router := http.NewServeMux()

	orderService := service.NewOrderService()
	orderHandler := handler.NewHttpOrdersHandler(orderService)
	orderHandler.RegisterRouter(router)

	log.Println("Starting server on", server.addr)

	return http.ListenAndServe(server.addr, router)
}
