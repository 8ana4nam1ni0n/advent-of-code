package day10

import "testing"

func TestSolutionPart1(t *testing.T) {

	input_file := "../aoc_inputs/day10/test"

	expected := 36
	result, _ := Solution(input_file)

	if result != expected {
		t.Errorf("expected %d, got %d", expected, result)
	}
}

func TestSolutionPart2(t *testing.T) {

	input_file := "../aoc_inputs/day10/test"

	expected := 81
	_, result := Solution(input_file)

	if result != expected {
		t.Errorf("expected %d, got %d", expected, result)
	}
}
