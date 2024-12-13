package day07

import (
	"goaoc/utils"
	"math"
	"strconv"
	"strings"
)

type Calibration struct {
	Target   int
	Equation []int
}

func getData(filename string) []Calibration {
	data := utils.ReadInputFile(filename)
	lines := strings.Split(strings.TrimSpace(data), "\n")
	var calibrations []Calibration

	for _, line := range lines {
		content := strings.Split(line, ":")
		target, _ := strconv.Atoi(content[0])
		equation := strings.Split(strings.TrimSpace(content[1]), " ")
		calibrations = append(calibrations,
			Calibration{
				Target: target,
				Equation: utils.Map(equation, func(n string) int {
					asNum, _ := strconv.Atoi(n)
					return asNum
				}),
			})
	}
	return calibrations
}

func checkCalibration(calibration Calibration) bool {
	var q [][]int
	q = append(q, []int{calibration.Equation[0], 1})
	equationLen := len(calibration.Equation)
	for len(q) > 0 {
		current, next := q[0][0], q[0][1]
		q = q[1:]
		if current == calibration.Target && next == equationLen {
			return true
		}
		if next == equationLen {
			continue
		}

		q = append(q, []int{current + calibration.Equation[next], next + 1})
		q = append(q, []int{current * calibration.Equation[next], next + 1})
	}
	return false
}

func concatenateNumbers(a, b int) int {
	if b == 0 {
		return a * 10
	}
	digitCount := int(math.Log10(float64(b))) + 1
	return a*int(math.Pow10(digitCount)) + b
}

func checkCalibration2(calibration Calibration) bool {
	var q [][]int
	q = append(q, []int{calibration.Equation[0], 1})
	equationLen := len(calibration.Equation)
	for len(q) > 0 {
		current, next := q[0][0], q[0][1]
		q = q[1:]
		if current == calibration.Target && next == equationLen {
			return true
		}
		if next == equationLen {
			continue
		}

		q = append(q, []int{current + calibration.Equation[next], next + 1})
		q = append(q, []int{current * calibration.Equation[next], next + 1})
		q = append(q, []int{concatenateNumbers(current, calibration.Equation[next]), next + 1})
	}
	return false
}

func SolutionPart1(filename string) int {
	calibrations := getData(filename)
	result := 0

	for _, calibration := range calibrations {
		if checkCalibration(calibration) {
			result += calibration.Target
		}
	}
	return result
}

func SolutionPart2(filename string) int {
	calibrations := getData(filename)
	result := 0

	for _, calibration := range calibrations {
		if checkCalibration2(calibration) {
			result += calibration.Target
		}
	}
	return result
}
