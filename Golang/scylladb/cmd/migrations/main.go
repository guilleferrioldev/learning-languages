package main

import (
	"context"
	"os"

	"github.com/scylladb/gocqlx/v3/migrate"

	"reporting/config"
	"reporting/scylla"
)

func main() {
	ctx := context.Background()

	cfg, err := config.Load()
	if err != nil {
		panic(err)
	}

	manager := scylla.NewManager(cfg)

	if err = manager.CreateKeyspace(cfg.ScyllaKeyspace); err != nil {
		panic(err)
	}

	session, err := manager.Connect()
	if err != nil {
		panic(err)
	}

	if err = migrate.FromFS(ctx, session, os.DirFS(cfg.ScyllaMigrationsDir)); err != nil {
		panic(err)
	}
}
