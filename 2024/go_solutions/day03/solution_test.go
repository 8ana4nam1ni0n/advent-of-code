package day03

import (
	"testing"
)

func TestSolutionPart1(t *testing.T) {

	input_file := "../aoc_inputs/day03/test"

	expected := 161
	result := SolutionPart1(input_file)

	if result != expected {
		t.Errorf("expected %q, got %q", expected, result)
	}

}

func TestSolutionPart2(t *testing.T) {

	input_file := "../aoc_inputs/day03/test"

	expected := 48
	result := SolutionPart2(input_file)

	if result != expected {
		t.Errorf("expected %q, got %q", expected, result)
	}

}
