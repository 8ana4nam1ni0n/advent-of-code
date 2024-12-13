package utils

func Count[T comparable](slice []T, target T) int {
	var count int
	for _, t := range slice {
		if t == target {
			count++
		}
	}
	return count
}
