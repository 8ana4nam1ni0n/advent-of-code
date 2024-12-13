package day04

import (
	"goaoc/utils"
	"strings"
)

func getData(filename string) [][]rune {
	data := utils.ReadInputFile(filename)
	lines := strings.Split(strings.TrimSpace(data), "\n")
	matrix := make([][]rune, len(lines))
	for i, line := range lines {
		matrix[i] = []rune(line)
	}
	return matrix
}

var directions = [][2]int{
	{0, 1}, {0, -1}, {1, 0}, {-1, 0}, {1, 1}, {1, -1}, {-1, 1}, {-1, -1},
}

func searchWordInDirection(matrix [][]rune, word string, starting_position [2]int, direction [2]int) bool {
	row_start, col_start := starting_position[0], starting_position[1]
	delta_row, delta_col := direction[0], direction[1]

	for i, character := range word {
		x := row_start + i*delta_row
		y := col_start + i*delta_col

		if x < 0 || x >= len(matrix) || y < 0 || y >= len(matrix[0]) {
			return false
		}

		if matrix[x][y] != character {
			return false
		}
	}
	return true
}

func wordSearchCounter(matrix [][]rune, word string) int {
	rows := len(matrix)
	cols := len(matrix[0])
	word_count := 0

	for r := 0; r < rows; r++ {
		for c := 0; c < cols; c++ {
			if matrix[r][c] == rune(word[0]) {
				current_position := [2]int{r, c}
				for _, direction := range directions {
					if searchWordInDirection(matrix, word, current_position, direction) {
						word_count++
					}
				}
			}
		}
	}
	return word_count
}

func SolutionPart1(filename string) int {
	matrix := getData(filename)
	return wordSearchCounter(matrix, "XMAS")
}

var x_directions = [][2]int{{1, 1}, {1, -1}}

func SolutionPart2(filename string) int {
	matrix := getData(filename)
	rows := len(matrix)
	cols := len(matrix[0])
	x_mas_count := 0

	for r := 1; r <= rows-1; r++ {
		for c := 1; c <= cols-1; c++ {
			if matrix[r][c] == 'A' {
				front_diagonal := [2]int{r - 1, c - 1}
				back_diagonal := [2]int{r - 1, c + 1}
				fd_found := searchWordInDirection(matrix, "MAS", front_diagonal, x_directions[0])
				fd_found_reversed := searchWordInDirection(matrix, "SAM", front_diagonal, x_directions[0])
				bd_found := searchWordInDirection(matrix, "MAS", back_diagonal, x_directions[1])
				bd_found_reversed := searchWordInDirection(matrix, "SAM", back_diagonal, x_directions[1])

				if (fd_found || fd_found_reversed) && (bd_found || bd_found_reversed) {
					x_mas_count++
				}
			}
		}
	}
	return x_mas_count
}
