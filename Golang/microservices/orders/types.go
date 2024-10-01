package main

import (
	pb "commons/api"
	"context"
)

type OrdersService interface {
	CreateOrder(context.Context) error
	validateIOrders(context.Context, pb.CreateOrderRequest) error
}

type OrderStore interface {
	Create(context.Context) error
}
