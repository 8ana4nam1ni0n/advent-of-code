package main

import (
	"fmt"
	"goaoc/day01"
	"goaoc/day02"
	"goaoc/day03"
	"goaoc/day04"
	"goaoc/day05"
	"goaoc/day06"
	"goaoc/day07"
	"goaoc/day08"
	"goaoc/day09"
	"goaoc/day10"
	"goaoc/day11"
	"os"
	"strconv"
)

func main() {

	if len(os.Args) < 2 {
		fmt.Println("Missing day argument")
		os.Exit(1)
	}

	dayArg := os.Args[1]
	day, err := strconv.Atoi(dayArg)
	if err != nil {
		fmt.Println("Argument day has to be an integer")
		os.Exit(1)
	}
	filename := fmt.Sprintf("aoc_inputs/day%02d/input", day)

	switch day {
	case 1:
		fmt.Println("Day 1 I: ", day01.SolutionPart1(filename))
		fmt.Println("Day 1 II: ", day01.SolutionPart2(filename))
	case 2:
		fmt.Println("Day 2 I: ", day02.SolutionPart1(filename))
		fmt.Println("Day 2 II: ", day02.SolutionPart2(filename))
	case 3:
		fmt.Println("Day 3 I: ", day03.SolutionPart1(filename))
		fmt.Println("Day 3 II: ", day03.SolutionPart2(filename))
	case 4:
		fmt.Println("Day 4 I: ", day04.SolutionPart1(filename))
		fmt.Println("Day 4 II: ", day04.SolutionPart2(filename))
	case 5:
		fmt.Println("Day 5 I: ", day05.SolutionPart1(filename))
		fmt.Println("Day 5 II: ", day05.SolutionPart2(filename))
	case 6:
		fmt.Println("Day 6 I: ", day06.SolutionPart1(filename))
		fmt.Println("Day 6 II: ", day06.SolutionPart2(filename))
	case 7:
		fmt.Println("Day 7 I: ", day07.SolutionPart1(filename))
		fmt.Println("Day 7 II: ", day07.SolutionPart2(filename))
	case 8:
		fmt.Println("Day 8 I: ", day08.SolutionPart1(filename))
		fmt.Println("Day 8 II: ", day08.SolutionPart2(filename))
	case 9:
		fmt.Println("Day 9 I: ", day09.SolutionPart1(filename))
		fmt.Println("Day 9 II: ", day09.SolutionPart2(filename))
	case 10:
		part1, part2 := day10.Solution(filename)
		fmt.Println("Day 10 I: ", part1)
		fmt.Println("Day 10 II: ", part2)
	case 11:
		fmt.Println("Day 11 I: ", day11.SolutionPart1(filename))
		fmt.Println("Day 11 II: ", day11.SolutionPart2(filename))
	default:
		fmt.Println("day not found")
	}
}
