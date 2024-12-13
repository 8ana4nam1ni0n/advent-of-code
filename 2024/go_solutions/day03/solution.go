package day03

import (
	"goaoc/utils"
	"regexp"
	"strconv"
)

func getData(filename string) string {
	return utils.ReadInputFile(filename)
}

func SolutionPart1(filename string) int {
	data := getData(filename)
	pattern := `mul\((\d{1,3}),(\d{1,3})\)`
	re := regexp.MustCompile(pattern)

	matches := re.FindAllStringSubmatch(data, -1)

	var product int
	for _, match := range matches {
		n, _ := strconv.Atoi(match[1])
		m, _ := strconv.Atoi(match[2])

		product += n * m
	}

	return product
}

func SolutionPart2(filename string) int {
	data := getData(filename)
	enable_pattern := `do\(\)`
	disable_pattern := `don't\(\)`
	pattern := `mul\((\d{1,3}),(\d{1,3})\)`
	re := regexp.MustCompile(pattern)
	reEnable := regexp.MustCompile(enable_pattern)
	reDisable := regexp.MustCompile(disable_pattern)

	enable_matches := reEnable.FindAllStringSubmatchIndex(data, -1)
	disable_matches := reDisable.FindAllStringSubmatchIndex(data, -1)
	matches := re.FindAllStringSubmatchIndex(data, -1)

	var product int

	enabled := true
	for _, match := range matches {
		start := match[0]

		if len(enable_matches) > 0 && start >= enable_matches[0][0] {
			enabled = true
			enable_matches = enable_matches[1:]
		} else if len(disable_matches) > 0 && start >= disable_matches[0][0] {
			enabled = false
			disable_matches = disable_matches[1:]
		}

		if enabled {
			tokenA, _ := strconv.Atoi(data[match[2]:match[3]])
			tokenB, _ := strconv.Atoi(data[match[4]:match[5]])
			product += tokenA * tokenB
		}
	}
	return product
}
