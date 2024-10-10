package uuid

import "testing"

func TestGenerate(t *testing.T) {
	g := New()
	uuidStr := g.Generate()
	if err := g.Parse(uuidStr); err != nil {
		t.Errorf("Error parsing generated uuid: %s", err)
	}
}
