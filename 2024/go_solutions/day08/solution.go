package day08

import (
	"fmt"
	"goaoc/utils"
	"strings"
)

type Antenna struct {
	X, Y int
}

func getData(filename string) (map[string][]Antenna, int) {
	data := utils.ReadInputFile(filename)
	lines := strings.Split(strings.TrimSpace(data), "\n")
	antennas := make(map[string][]Antenna)

	for r, line := range lines {
		for c, char := range line {
			antenna := string(char)
			if char == '.' {
				continue
			}
			antennas[antenna] = append(antennas[antenna], Antenna{X: r, Y: c})
		}
	}
	return antennas, len(lines)
}

func getAntinodes(antennas map[string][]Antenna) map[Antenna]bool {
	antinodes := make(map[Antenna]bool)

	for _, freqCoords := range antennas {
		for i := 0; i < len(freqCoords); i++ {
			for j := i + 1; j < len(freqCoords); j++ {
				dx := freqCoords[j].X - freqCoords[i].X
				dy := freqCoords[j].Y - freqCoords[i].Y

				antinode_1 := Antenna{freqCoords[i].X - dx, freqCoords[i].Y - dy}
				antinode_2 := Antenna{freqCoords[j].X + dx, freqCoords[j].Y + dy}

				antinodes[antinode_1] = true
				antinodes[antinode_2] = true
			}
		}
	}
	return antinodes
}

func filterOutOfGrid(antinodes map[Antenna]bool, gridLength int) {
	for antinode := range antinodes {
		if antinode.X < 0 || antinode.Y < 0 || antinode.X >= gridLength || antinode.Y >= gridLength {
			delete(antinodes, antinode)
		}
	}
}

func drawAntinodes(antinodes map[Antenna]bool, gridLength int) {
	grid := make([][]string, gridLength)
	for i := range grid {
		grid[i] = make([]string, gridLength)
	}

	for i := 0; i < gridLength; i++ {
		for j := 0; j < gridLength; j++ {
			grid[i][j] = "."
		}
	}
	for antinodes := range antinodes {
		grid[antinodes.X][antinodes.Y] = "#"
	}

	for _, g := range grid {
		fmt.Println(g)
	}
}

func SolutionPart1(filename string) int {
	antennas, gridLength := getData(filename)
	antinodes := getAntinodes(antennas)

	filterOutOfGrid(antinodes, gridLength)

	return len(antinodes)
}

func getAntinodes2(antennas map[string][]Antenna, gridLength int) map[Antenna]bool {
	antinodes := make(map[Antenna]bool)

	for _, freqCoords := range antennas {
		for i := 0; i < len(freqCoords); i++ {
			for j := 0; j < len(freqCoords); j++ {
				if i == j {
					continue
				}
				dx := freqCoords[j].X - freqCoords[i].X
				dy := freqCoords[j].Y - freqCoords[i].Y

				r := freqCoords[i].X
				c := freqCoords[i].Y
				for 0 <= r && 0 <= c && r < gridLength && c < gridLength {
					antinodes[Antenna{r, c}] = true
					r += dx
					c += dy
				}
			}
		}
	}
	return antinodes
}

func SolutionPart2(filename string) int {
	antennas, gridLength := getData(filename)
	fmt.Println(antennas, gridLength)
	antinodes := getAntinodes2(antennas, gridLength)

	drawAntinodes(antinodes, gridLength)

	return len(antinodes)
}
