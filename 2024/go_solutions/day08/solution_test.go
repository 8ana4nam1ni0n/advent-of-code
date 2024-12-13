package day08

import "testing"

func TestSolutionPart1(t *testing.T) {

	input_file := "../aoc_inputs/day08/test"

	expected := 14
	result := SolutionPart1(input_file)

	if result != expected {
		t.Errorf("expected %d, got %d", expected, result)
	}
}

func TestSolutionPart2(t *testing.T) {

	input_file := "../aoc_inputs/day08/test"

	expected := 34
	result := SolutionPart2(input_file)

	if result != expected {
		t.Errorf("expected %d, got %d", expected, result)
	}
}
