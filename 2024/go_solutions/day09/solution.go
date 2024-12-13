package day09

import (
	"goaoc/utils"
	"strconv"
	"strings"
)

func getData(filename string) string {
	return strings.TrimSpace(utils.ReadInputFile(filename))
}

func expand(disk string) []string {
	id := 0
	var expanded []string
	for pos, block := range disk {
		n := int(block - '0')
		for i := 0; i < n; i++ {
			if pos%2 == 0 {
				expanded = append(expanded, strconv.Itoa(id))
			} else {
				expanded = append(expanded, ".")
			}
		}
		if pos%2 == 0 {
			id++
		}
	}
	return expanded
}

func compress(disk *[]string) {
	var freeSpaceIndex []int
	diskptr := (*disk)
	for i := range diskptr {
		if diskptr[i] == "." {
			freeSpaceIndex = append(freeSpaceIndex, i)
		}
	}

	tail := len(diskptr) - 1
	for _, index := range freeSpaceIndex {
		for diskptr[tail] == "." {
			utils.PopBack(disk)
			tail--
		}
		if tail <= index {
			break
		}
		diskptr[index], _ = utils.PopBack(disk)
		tail--
	}
}

func calculateChecksum(disk []string) int {
	checksum := 0
	for i, id := range disk {
		if id == "." {
			continue
		}
		n, _ := strconv.Atoi(id)
		checksum += i * n
	}
	return checksum
}

func SolutionPart1(filename string) int {
	diskMap := getData(filename)

	// fmt.Println(disk)
	expanded := expand(diskMap)
	// fmt.Println(expanded)

	compress(&expanded)
	// fmt.Println(expanded)

	return calculateChecksum(expanded)
}

type Block struct {
	Index int
	Size  int
}

func getFreeSpaceBlocks(diskMap []string) []Block {
	var freeSpaceBlocks []Block
	for i := 0; i < len(diskMap); i++ {
		if diskMap[i] == "." {
			index := i + 1
			size := 1
			for diskMap[index] == "." {
				size++
				index++
			}
			index--
			freeSpaceBlocks = append(freeSpaceBlocks, Block{i, size})
			i = index
		}
	}
	return freeSpaceBlocks
}

func getFileBlocks(diskMap []string) []Block {
	var fileBlocks []Block
	for i := 0; i < len(diskMap); i++ {
		if diskMap[i] == "." {
			continue
		}
		id := diskMap[i]
		index := i + 1
		size := 1
		for index < len(diskMap) && diskMap[index] == id {
			size++
			index++
		}
		index--
		fileBlocks = append(fileBlocks, Block{i, size})
		i = index
	}
	return fileBlocks
}

func reverse(slice []Block) chan Block {
	ret := make(chan Block)
	go func() {
		for i := range slice {
			ret <- slice[len(slice)-1-i]
		}
		close(ret)
	}()
	return ret
}

func allocateBlocksToFreeSpace(diskMap *[]string) {
	freeBlocks := getFreeSpaceBlocks(*diskMap)
	fileBlocks := getFileBlocks(*diskMap)

	for fblock := range reverse(fileBlocks) {
		fidx := fblock.Index
		fsize := fblock.Size
		for i, freeBlock := range freeBlocks {
			bidx := freeBlock.Index
			bsize := freeBlock.Size
			if bidx >= fidx {
				break
			}
			if fsize <= bsize {
				for bsize > 0 && fsize > 0 {
					(*diskMap)[bidx] = (*diskMap)[fidx+fsize-1]
					(*diskMap)[fidx+fsize-1] = "."
					fsize--
					bsize--
					bidx++
				}
				freeBlocks[i].Size = bsize
				freeBlocks[i].Index = bidx
			}
		}
	}
}

func SolutionPart2(filename string) int {
	diskMap := getData(filename)
	expanded := expand(diskMap)
	allocateBlocksToFreeSpace(&expanded)
	return calculateChecksum(expanded)
}
