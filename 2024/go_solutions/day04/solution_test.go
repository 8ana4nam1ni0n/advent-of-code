package day04

import (
	"testing"
)

func TestSolutionPart1(t *testing.T) {

	input_file := "../aoc_inputs/day04/test"

	expected := 18
	result := SolutionPart1(input_file)

	if result != expected {
		t.Errorf("expected %q, got %q", expected, result)
	}

}

func TestSolutionPart2(t *testing.T) {

	input_file := "../aoc_inputs/day04/test"

	expected := 9
	result := SolutionPart2(input_file)

	if result != expected {
		t.Errorf("expected %q, got %q", expected, result)
	}

}
