//go:generate mockgen -source=uuid.go -destination=mock/uuid_mock.go -package=mock
package uuid

type Generator interface {
	Generate() string
	Parse(uuidStr string) error
}

func New() Generator {
	return &generator{}
}
