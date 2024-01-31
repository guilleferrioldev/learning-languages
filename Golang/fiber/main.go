package main

import (
	"github.com/gofiber/fiber/v2"
	"github.com/google/uuid"
)

type User struct {
	id       string
	fistname string
	lastname string
}

func handleUser(c *fiber.Ctx) error {
	user := User{
		fistname: "Joe",
		lastname: "Doe",
	}
	return c.Status(fiber.StatusOK).JSON(user)
}

func handleCreateUser(c *fiber.Ctx) error {
	user := User{}
	if err := c.BodyParser(&user); err != nil {
		return err
	}

	user.id = uuid.NewString()

	return c.Status(fiber.StatusOK).JSON(user)
}

func main() {
	app := fiber.New()

	app.Get("/", func(c *fiber.Ctx) error {
		return c.SendString("Hello, World!")
	})

	userGroup := app.Group("/users")

	userGroup.Get("", handleUser)
	userGroup.Post("", handleCreateUser)

	app.Listen(":3000")
}
