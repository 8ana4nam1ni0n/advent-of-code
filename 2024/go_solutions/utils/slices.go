package utils

func PopBack[T any](slice *[]T) (T, bool) {
	if len(*slice) == 0 {
		var zero T
		return zero, false
	}
	popped := (*slice)[len(*slice)-1]
	(*slice) = (*slice)[:len(*slice)-1]
	return popped, true
}
