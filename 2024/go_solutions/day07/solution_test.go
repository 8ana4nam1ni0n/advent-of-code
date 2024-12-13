package day07

import "testing"

func TestSolutionPart1(t *testing.T) {

	input_file := "../aoc_inputs/day07/test"

	expected := 3749
	result := SolutionPart1(input_file)

	if result != expected {
		t.Errorf("expected %d, got %d", expected, result)
	}
}

func TestSolutionPart2(t *testing.T) {

	input_file := "../aoc_inputs/day07/test"

	expected := 11387
	result := SolutionPart2(input_file)

	if result != expected {
		t.Errorf("expected %d, got %d", expected, result)
	}
}
