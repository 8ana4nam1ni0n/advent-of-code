package day11

import "testing"

func TestSolutionPart1(t *testing.T) {

	input_file := "../aoc_inputs/day11/test"

	expected := 5532
	result := SolutionPart1(input_file)

	if result != expected {
		t.Errorf("expected %d, got %d", expected, result)
	}
}

func TestSolutionPart2(t *testing.T) {

	input_file := "../aoc_inputs/day11/test"

	expected := 1
	result := SolutionPart2(input_file)

	if result != expected {
		t.Errorf("expected %d, got %d", expected, result)
	}
}
