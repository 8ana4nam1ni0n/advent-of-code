package day06

import (
	"goaoc/utils"
	"slices"
	"strings"
)

type Guard struct {
	row, col  int
	direction int
}

var directions = [][2]int{{-1, 0}, {0, 1}, {1, 0}, {0, -1}}

func getData(filename string) [][]rune {
	data := utils.ReadInputFile(filename)
	lines := strings.Split(strings.TrimSpace(data), "\n")
	grid := make([][]rune, len(lines))
	for i, line := range lines {
		grid[i] = []rune(line)
	}
	return grid
}

func getStartingPoint(grid [][]rune) Guard {
	r, c := 0, 0
	for i, chars := range grid {
		if c = slices.Index(chars, '^'); c >= 0 {
			r = i
			break
		}
	}
	return Guard{row: r, col: c, direction: 0}
}

func isInside(grid [][]rune, guard Guard) bool {
	r := guard.row + directions[guard.direction][0]
	c := guard.col + directions[guard.direction][1]
	l := len(grid)
	return r >= 0 && r < l && c >= 0 && c < l
}

func SolutionPart1(filename string) int {
	grid := getData(filename)
	guard := getStartingPoint(grid)
	visited := make(map[[2]int]bool)
	visited[[2]int{guard.row, guard.col}] = true

	for isInside(grid, guard) {
		r := guard.row + directions[guard.direction][0]
		c := guard.col + directions[guard.direction][1]

		if grid[r][c] == '#' {
			guard.direction = (guard.direction + 1) % 4
			continue
		}
		visited[[2]int{r, c}] = true
		guard.row = r
		guard.col = c
	}
	return len(visited)
}

func isLoop(grid [][]rune, guard Guard) bool {
	current := guard
	visited := make(map[Guard]bool)

	for {
		if visited[current] {
			return true
		}
		visited[current] = true

		nextRow := current.row + directions[current.direction][0]
		nextCol := current.col + directions[current.direction][1]

		if nextRow < 0 || nextRow >= len(grid) || nextCol < 0 || nextCol >= len(grid) {
			return false
		}

		if grid[nextRow][nextCol] == '#' {
			current.direction = (current.direction + 1) % 4
		} else {
			current.row = nextRow
			current.col = nextCol
		}
	}
}

func SolutionPart2(filename string) int {
	grid := getData(filename)
	guard := getStartingPoint(grid)
	loops := 0

	for r := 0; r < len(grid); r++ {
		for c := 0; c < len(grid); c++ {
			if grid[r][c] == '.' {
				grid[r][c] = '#'
				if isLoop(grid, guard) {
					loops++
				}
				grid[r][c] = '.'
			}
		}
	}
	return loops
}
