package day02

import (
	"testing"
)

func TestSolutionPart1(t *testing.T) {

	input_file := "../aoc_inputs/day02/test"

	expected := 2
	result := SolutionPart1(input_file)

	if result != expected {
		t.Errorf("expected %q, got %q", expected, result)
	}

}

func TestSolutionPart2(t *testing.T) {

	input_file := "../aoc_inputs/day02/test"

	expected := 4
	result := SolutionPart2(input_file)

	if result != expected {
		t.Errorf("expected %q, got %q", expected, result)
	}

}
