package router

import (
	"react-go-crud/controller"

	"github.com/gofiber/fiber/v2"
)

// Setup routing information
func SetupRoutes(app *fiber.App) {
	// list => get
	app.Get("/", controller.BlogList)

	// add => post
	app.Post("/", controller.BlogCreate)

	// update => put
	app.Put("/:id", controller.BlogUpdate)

	// delete => delete
	app.Delete("/:id", controller.BlogDelete)
}
