package utils

func Map[T any, R any](data []T, fn func(T) R) []R {
	var result []R
	for _, d := range data {
		result = append(result, fn(d))
	}
	return result
}

func Sum(list []int) int {
	var result int
	for _, n := range list {
		result += n
	}
	return result
}

func Filter[T any](data []T, fn func(T) bool) []T {
	var filtered []T
	for _, d := range data {
		if fn(d) {
			filtered = append(filtered, d)
		}
	}
	return filtered
}
