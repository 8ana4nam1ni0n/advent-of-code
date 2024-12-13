package day11

import (
	"fmt"
	"goaoc/utils"
	"math"
	"strconv"
	"strings"
)

func getData(filename string) []int {
	data := utils.ReadInputFile(filename)
	tokens := strings.Fields(strings.TrimSpace(data))

	return utils.Map(tokens, func(t string) int {
		n, _ := strconv.Atoi(t)
		return n
	})
}

func getDigitCount(n int) int {
	return int(math.Log10(float64(n))) + 1
}

func hasEvenDigits(n int) bool {
	return getDigitCount(n)%2 == 0
}

type Tuple struct {
	First  int
	Second int
}

func splitDigits(n int) Tuple {
	halfDigitCount := getDigitCount(n) / 2
	mask := int(math.Pow10(halfDigitCount))
	return Tuple{First: n / mask, Second: n % mask}
}

func blink(times int, stones []int) *utils.List[int] {
	stoneList := utils.NewList[int]()

	for _, stone := range stones {
		stoneList.Add(stone)
	}

	for i := 0; i < times; i++ {
		for {
		}
	}

	return stoneList
}

func SolutionPart1(filename string) int {
	stones := getData(filename)

	blink(5, stones).Display()

	return 1
}

func SolutionPart2(filename string) int {
	stones := getData(filename)
	fmt.Println(stones)

	return 1
}
