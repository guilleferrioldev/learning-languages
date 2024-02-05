package main

import (
	"log"
	"os"
	"react-go-crud/database"
	"react-go-crud/router"

	"github.com/gofiber/fiber/v2"
	"github.com/joho/godotenv"
)

func init() {
	err := godotenv.Load(".env")
	if err != nil {
		log.Fatal(err)
	}

	config := &database.Config{
		Host:     os.Getenv("DB_HOST"),
		Port:     os.Getenv("DB_PORT"),
		Password: os.Getenv("DB_PASS"),
		User:     os.Getenv("DB_USER"),
		DBName:   os.Getenv("DB_NAME"),
		SSLMode:  os.Getenv("DB_SSLMODE"),
	}

	database.ConnectDB(config)
}

func main() {
	sqlDb, err := database.DBConn.DB()

	if err != nil {
		panic("Error in sql connection")
	}

	defer sqlDb.Close()

	app := fiber.New()
	router.SetupRoutes(app)
	app.Listen(":8000")
}
