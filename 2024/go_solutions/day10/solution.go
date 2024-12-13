package day10

import (
	"goaoc/utils"
	"strconv"
	"strings"
)

func getData(filename string) [][]int {
	data := utils.ReadInputFile(filename)
	lines := strings.Split(strings.TrimSpace(data), "\n")
	grid := make([][]int, 0, len(lines))

	for _, line := range lines {
		row := make([]int, 0, len(lines))
		for _, digit := range line {
			number, _ := strconv.Atoi(string(digit))
			row = append(row, number)
		}
		grid = append(grid, row)
	}
	return grid
}

type Coord struct {
	row int
	col int
}

func NewCoord(row int, col int) Coord {
	return Coord{row: row, col: col}
}

func getTrailHeadScore(pos Coord, grid [][]int, grid_size int) (int, int) {
	q := utils.NewQueue[Coord]()
	q.Enqueue(pos)
	visited := make(map[Coord]bool)
	rating := 0

	for !q.IsEmpty() {
		current, _ := q.Dequeue()
		r, c := current.row, current.col

		if grid[r][c] == 9 {
			visited[current] = true
			rating++
			continue
		}
		for _, d := range [][2]int{{0, -1}, {0, 1}, {1, 0}, {-1, 0}} {
			dr, dc := r+d[0], c+d[1]
			if dc < 0 || dc >= grid_size || dr < 0 || dr >= grid_size {
				continue
			}
			if grid[dr][dc]-grid[r][c] == 1 {
				q.Enqueue(NewCoord(dr, dc))
			}
		}
	}
	return len(visited), rating
}

func Solution(filename string) (int, int) {
	grid := getData(filename)
	grid_size := len(grid)

	var zeros []Coord

	for r := 0; r < grid_size; r++ {
		for c := 0; c < grid_size; c++ {
			if grid[r][c] == 0 {
				zeros = append(zeros, NewCoord(r, c))
			}
		}
	}

	var trailhead_scores []int
	var ratings []int
	for _, zero := range zeros {
		ts, rs := getTrailHeadScore(zero, grid, grid_size)
		trailhead_scores = append(trailhead_scores, ts)
		ratings = append(ratings, rs)
	}

	return utils.Sum(trailhead_scores), utils.Sum(ratings)
}
