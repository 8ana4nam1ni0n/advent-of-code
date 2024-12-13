package utils

type Q[T any] struct {
	items []T
}

func NewQueue[T any]() *Q[T] {
	return &Q[T]{items: make([]T, 0)}
}

func (q *Q[T]) Enqueue(item T) {
	q.items = append(q.items, item)
}

func (q *Q[T]) Dequeue() (T, bool) {
	var zero T
	if len(q.items) == 0 {
		return zero, false
	}
	item := q.items[0]
	q.items = q.items[1:]
	return item, true
}

func (q *Q[T]) IsEmpty() bool {
	return len(q.items) == 0
}

func (q *Q[T]) Size() int {
	return len(q.items)
}
