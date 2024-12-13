package day09

import "testing"

func TestSolutionPart1(t *testing.T) {

	input_file := "../aoc_inputs/day09/test"

	expected := 1928
	result := SolutionPart1(input_file)

	if result != expected {
		t.Errorf("expected %d, got %d", expected, result)
	}
}

func TestSolutionPart2(t *testing.T) {

	input_file := "../aoc_inputs/day09/test"

	expected := 2858
	result := SolutionPart2(input_file)

	if result != expected {
		t.Errorf("expected %d, got %d", expected, result)
	}
}
