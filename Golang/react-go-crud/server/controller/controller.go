package controller

import (
	"log"
	"react-go-crud/database"
	"react-go-crud/model"
	"time"

	"github.com/gofiber/fiber/v2"
)

// Blog List
func BlogList(c *fiber.Ctx) error {

	var context = fiber.Map{"statusText": "OK",
		"message": "Blog List"}
	var records []model.Blog

	time.Sleep(time.Millisecond * 100)

	db := database.DBConn
	db.Find(&records)
	context["blog_records"] = records

	return c.Status(200).JSON(context)
}

// Blog detail page
func BlogDetail(c *fiber.Ctx) error {
	c.Status(400)
	context := fiber.Map{"statusText": "",
		"message": ""}

	id := c.Params("id")
	var record model.Blog

	database.DBConn.First(&record, id)

	if record.ID == 0 {
		log.Println("Record not Found")
		context["message"] = "Record not Found"
		return c.Status(404).JSON(context)
	}

	context["record"] = record
	context["statusText"] = "OK"
	context["message"] = "Blog Detail"
	return c.Status(200).JSON(context)
}

// Add Blog into database
func BlogCreate(c *fiber.Ctx) error {
	var context = fiber.Map{"statusText": "OK",
		"message": "Add a Blog"}

	record := new(model.Blog)

	if err := c.BodyParser(&record); err != nil {
		log.Println("Error in parsing request")
		context["statusText"] = ""
		context["message"] = "Something went wrong"
	}

	result := database.DBConn.Create(record)

	if result.Error != nil {
		log.Panicln("Error in saving data")
	}

	context["message"] = "Record is saved successfully"
	context["data"] = record

	return c.Status(201).JSON(context)
}

// Update a Blog
func BlogUpdate(c *fiber.Ctx) error {
	context := fiber.Map{"statusText": "OK",
		"message": "Update Blog"}

	id := c.Params("id")
	var record model.Blog

	database.DBConn.First(&record, id)

	if record.ID == 0 {
		log.Println("Record not Found")
		context["statusText"] = ""
		context["message"] = "Record not Found"
		return c.Status(400).JSON(context)
	}

	if err := c.BodyParser(&record); err != nil {
		log.Println("Error in parsing request")
	}

	result := database.DBConn.Save(record)

	if result.Error != nil {
		log.Println("Error in saving data")
	}

	context["message"] = "Record update successfully"
	context["data"] = record

	return c.Status(200).JSON(context)
}

// Delete a Blog
func BlogDelete(c *fiber.Ctx) error {
	c.Status(400)
	context := fiber.Map{"statusText": "",
		"message": ""}

	id := c.Params("id")
	var record model.Blog

	database.DBConn.First(&record, id)

	if record.ID == 0 {
		log.Println("Record not Found")
		context["message"] = "Record not Found"
		return c.JSON(context)
	}

	result := database.DBConn.Delete(record)

	if result.Error != nil {
		context["message"] = "Something went wrong"
		return c.JSON(context)
	}

	context["statusText"] = "OK"
	context["message"] = "Record delete successfully"
	return c.Status(200).JSON(context)
}
