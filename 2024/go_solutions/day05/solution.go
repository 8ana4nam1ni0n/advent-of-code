package day05

import (
	"goaoc/utils"
	"slices"
	"strconv"
	"strings"
)

func getData(filename string) ([][]int, [][]int) {
	data := utils.ReadInputFile(filename)
	sections := strings.Split(data, "\n\n")

	section_1_lines := strings.Split(strings.TrimSpace(sections[0]), "\n")
	section_2_lines := strings.Split(strings.TrimSpace(sections[1]), "\n")

	var rules [][]int
	var updates [][]int

	for _, lines := range section_1_lines {
		content := strings.Split(lines, "|")
		rule1, _ := strconv.Atoi(content[0])
		rule2, _ := strconv.Atoi(content[1])
		rules = append(rules, []int{rule1, rule2})
	}

	for _, lines := range section_2_lines {
		content := strings.Split(lines, ",")
		update := utils.Map(content, func(str string) int {
			n, _ := strconv.Atoi(str)
			return n
		})
		updates = append(updates, update)
	}

	return rules, updates
}

func isUpdateValid(rules [][]int, update []int) bool {
	for _, rule := range rules {
		r1, r2 := rule[0], rule[1]
		if slices.Contains(update, r1) && slices.Contains(update, r2) {
			index1 := slices.Index(update, r1)
			index2 := slices.Index(update, r2)
			if index1 > index2 {
				return false
			}
		}
	}
	return true
}

func SolutionPart1(filename string) int {
	rules, updates := getData(filename)

	var valid_updates []int
	for _, update := range updates {
		if isUpdateValid(rules, update) {
			middle := update[len(update)/2]
			valid_updates = append(valid_updates, middle)
		}
	}

	return utils.Sum(valid_updates)
}

func SolutionPart2(filename string) int {
	rules, updates := getData(filename)

	first_map := make(map[int][]int)
	second_map := make(map[int][]int)

	for _, rule := range rules {
		first, second := rule[0], rule[1]
		first_map[first] = append(first_map[first], second)
		second_map[second] = append(second_map[second], first)
	}

	var fixed_updates []int
	for _, update := range updates {
		if !isUpdateValid(rules, update) {

			slices.SortFunc(update, func(a, b int) int {
				if slices.Contains(first_map[a], b) {
					return -1
				} else if slices.Contains(second_map[b], a) {
					return 1
				} else {
					return 0
				}
			})

			middle := update[len(update)/2]
			fixed_updates = append(fixed_updates, middle)
		}
	}

	return utils.Sum(fixed_updates)
}
