package utils

import "fmt"

type Node[T comparable] struct {
	value T
	next  *Node[T]
}

type List[T comparable] struct {
	head *Node[T]
	size int
}

func NewList[T comparable]() *List[T] {
	return &List[T]{}
}

func (l *List[T]) Add(value T) {
	newNode := &Node[T]{value: value, next: nil}
	if l.head == nil {
		l.head = newNode
	} else {
		traverse := l.head
		for traverse.next != nil {
			traverse = traverse.next
		}
		traverse.next = newNode
	}
	l.size++
}

func (l *List[T]) Remove(value T) bool {
	if l.head == nil {
		return false
	}

	if l.head.value == value {
		l.head = l.head.next
		l.size--
		return true
	}

	prev := l.head
	curr := l.head.next
	for curr != nil {
		if curr.value == value {
			prev.next = curr.next
			l.size--
			return true
		}
		prev = curr
		curr = curr.next
	}

	return false
}

func (l *List[t]) value() t {
	return l.head.value
}

func (l *List[T]) Size() int {
	return l.size
}

func (l *List[T]) Display() {
	curr := l.head
	for curr != nil {
		fmt.Printf("%v -> ", curr.value)
		curr = curr.next
	}
	fmt.Println(nil)
}
