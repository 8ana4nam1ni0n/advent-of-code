package utils

import (
	"log"
	"os"
)

func ReadInputFile(filename string) string {
	data, err := os.ReadFile(filename)
	if err != nil {
		log.Fatalf("File read error: %s", err)
	}
	return string(data)
}
