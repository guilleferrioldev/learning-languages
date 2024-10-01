package main

import (
	pb "commons/api"
	"context"
	"errors"
	"log"
)

type service struct {
	store OrderStore
}

func NewService(store OrderStore) *service {
	return &service{store}
}

func (s *service) CreateOrder(ctx context.Context) error {
	return nil
}

func (s *service) ValidateIOrders(ctx context.Context, req *pb.CreateOrderRequest) error {
	if len(req.Items) == 0 {
		return errors.New("items must have at least one item")
	}

	mergedItems := mergeItems(req.Items)
	log.Print(mergedItems)

	return nil
}

func mergeItems(items []*pb.ItemsWithQuantity) []*pb.ItemsWithQuantity {
	result := make([]*pb.ItemsWithQuantity, 0)

	for _, item := range items {
		found := false
		for _, r := range result {
			if r.ItemId == item.ItemId {
				r.Quantity += item.Quantity
				found = true
				break
			}
		}

		if !found {
			result = append(result, item)
		}
	}

	return result
}
