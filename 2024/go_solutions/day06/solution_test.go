package day06

import "testing"

func TestSolutionPart1(t *testing.T) {

	input_file := "../aoc_inputs/day06/test"

	expected := 41
	result := SolutionPart1(input_file)

	if result != expected {
		t.Errorf("expected %d, got %d", expected, result)
	}
}

func TestSolutionPart2(t *testing.T) {

	input_file := "../aoc_inputs/day06/test"

	expected := 6
	result := SolutionPart2(input_file)

	if result != expected {
		t.Errorf("expected %d, got %d", expected, result)
	}
}
