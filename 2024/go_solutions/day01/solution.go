package day01

import (
	"goaoc/utils"
	"sort"
	"strconv"
	"strings"
)

func getData(filename string) ([]int, []int) {
	data := utils.ReadInputFile(filename)
	lines := strings.Split(strings.TrimSpace(data), "\n")
	var list_1 []int
	var list_2 []int

	for _, line := range lines {
		numbers := utils.Map(strings.Fields(line), func(number string) int {
			asNumber, _ := strconv.Atoi(number)
			return asNumber
		})
		list_1 = append(list_1, numbers[0])
		list_2 = append(list_2, numbers[1])
	}
	return list_1, list_2
}

func SolutionPart1(filename string) int {
	list_1, list_2 := getData(filename)
	sort.Sort(sort.Reverse(sort.IntSlice(list_1)))
	sort.Sort(sort.Reverse(sort.IntSlice(list_2)))
	var result int
	for i := 0; i < len(list_1); i++ {
		difference := list_1[i] - list_2[i]
		mask := difference >> 31
		result += (difference + mask) ^ mask
	}
	return result
}

func SolutionPart2(filename string) int {
	locationIds, right_list := getData(filename)
	var similarity_score int
	frequencyMap := make(map[int]int)
	for _, locationId := range locationIds {
		_, exists := frequencyMap[locationId]
		if !exists {
			frequencyMap[locationId] = utils.Count(right_list, locationId)
		}
		similarity_score += locationId * frequencyMap[locationId]
	}
	return similarity_score
}
