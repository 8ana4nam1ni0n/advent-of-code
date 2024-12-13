package day02

import (
	"goaoc/utils"
	"strconv"
	"strings"
)

type Report struct {
	Levels []int
}

func (r Report) RemoveLevel(index int) Report {
	var newLevels []int
	newLevels = append(newLevels, r.Levels[:index]...)
	newLevels = append(newLevels, r.Levels[index+1:]...)
	return Report{Levels: newLevels}
}

func (r Report) isIncreasing() bool {
	current := r.Levels[0]
	for i := 1; i < len(r.Levels); i++ {
		if current > r.Levels[i] {
			return false
		}
		current = r.Levels[i]
	}
	return true
}

func (r Report) isDecreasing() bool {
	current := r.Levels[0]
	for i := 1; i < len(r.Levels); i++ {
		if current < r.Levels[i] {
			return false
		}
		current = r.Levels[i]
	}
	return true
}

func (r Report) IsSafe() bool {
	if !r.isDecreasing() && !r.isIncreasing() {
		return false
	}
	// checks for difference between reports
	for i := 1; i < len(r.Levels); i++ {
		diff := utils.Abs(r.Levels[i-1] - r.Levels[i])
		if diff < 1 || diff > 3 {
			return false
		}
	}
	return true
}

func getData(filename string) []Report {
	data := utils.ReadInputFile(filename)
	lines := strings.Split(strings.TrimSpace(data), "\n")
	var reports []Report

	for _, line := range lines {
		numbers := utils.Map(strings.Fields(line), func(number string) int {
			asNumber, _ := strconv.Atoi(number)
			return asNumber
		})
		report := Report{Levels: numbers}
		reports = append(reports, report)
	}
	return reports
}

func problemDampenerOnDifference(report Report) bool {
	errorIndex1, errorIndex2 := -1, -1
	for i := 1; i < len(report.Levels); i++ {
		diff := utils.Abs(report.Levels[i-1] - report.Levels[i])
		if diff < 1 || diff > 3 {
			errorIndex1 = i - 1
			errorIndex2 = i
			break
		}
	}

	if errorIndex1 >= 0 {
		reportA := report.RemoveLevel(errorIndex1)
		reportB := report.RemoveLevel(errorIndex2)
		return reportA.IsSafe() || reportB.IsSafe()
	}
	return false
}

func problemDampenerOnAscending(report Report) bool {
	current := report.Levels[0]
	errorIndex1, errorIndex2 := -1, -1
	for i := 1; i < len(report.Levels); i++ {
		if current > report.Levels[i] {
			errorIndex1 = i - 1
			errorIndex2 = i
			break
		}
		current = report.Levels[i]
	}

	if errorIndex1 >= 0 {
		reportA := report.RemoveLevel(errorIndex1)
		reportB := report.RemoveLevel(errorIndex2)
		return reportA.IsSafe() || reportB.IsSafe()
	}
	return false
}

func problemDampenerOnDescending(report Report) bool {
	current := report.Levels[0]
	errorIndex1, errorIndex2 := -1, -1
	for i := 1; i < len(report.Levels); i++ {
		if current < report.Levels[i] {
			errorIndex1 = i - 1
			errorIndex2 = i
			break
		}
		current = report.Levels[i]
	}

	if errorIndex1 >= 0 {
		reportA := report.RemoveLevel(errorIndex1)
		reportB := report.RemoveLevel(errorIndex2)
		return reportA.IsSafe() || reportB.IsSafe()
	}
	return false
}

func SolutionPart1(filename string) int {
	reports := getData(filename)

	var count int
	for _, report := range reports {
		if report.IsSafe() {
			count++
		}
	}
	return count
}

func SolutionPart2(filename string) int {
	reports := getData(filename)
	var unsafe []Report

	var count int
	for _, report := range reports {
		if report.IsSafe() {
			count++
		} else {
			unsafe = append(unsafe, report)
		}
	}

	for _, report := range unsafe {
		isSafeOnAscending := problemDampenerOnAscending(report)
		isSafeOnDescending := problemDampenerOnDescending(report)
		isSafeOnDifference := problemDampenerOnDifference(report)
		if isSafeOnAscending || isSafeOnDescending || isSafeOnDifference {
			count++
		}
	}

	return count
}
