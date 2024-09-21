package service

import (
	"context"
	"grpc-microservices/services/common/genproto/orders"
)

var ordersDB = make([]*orders.Order, 0)

type OrderService struct {
	//store
}

func NewOrderService() *OrderService {
	return &OrderService{}
}

func (service *OrderService) CreateOrder(ctx context.Context, order *orders.Order) error {
	ordersDB = append(ordersDB, order)
	return nil
}

func (service *OrderService) GetOrders(ctx context.Context) []*orders.Order {
	return ordersDB
}
