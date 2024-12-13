package day05

import (
	"testing"
)

func TestSolutionPart1(t *testing.T) {

	input_file := "../aoc_inputs/day05/test"

	expected := 143
	result := SolutionPart1(input_file)

	if result != expected {
		t.Errorf("expected %q, got %q", expected, result)
	}

}

func TestSolutionPart2(t *testing.T) {

	input_file := "../aoc_inputs/day05/test"

	expected := 123
	result := SolutionPart2(input_file)

	if result != expected {
		t.Errorf("expected %d, got %d", expected, result)
	}

}
