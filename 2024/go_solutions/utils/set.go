package utils

type Set[T comparable] struct {
	elements map[T]struct{}
}

func NewSet[T comparable]() *Set[T] {
	return &Set[T]{
		elements: make(map[T]struct{}),
	}
}

func (s *Set[T]) Add(element T) {
	s.elements[element] = struct{}{}
}

func (s *Set[T]) Remove(element T) {
	delete(s.elements, element)
}

func (s *Set[T]) Contains(element T) bool {
	_, exists := s.elements[element]
	return exists
}

func (s *Set[T]) Size() int {
	return len(s.elements)
}

func (s Set[T]) List() []T {
	list := make([]T, s.Size())
	for key := range s.elements {
		list = append(list, key)
	}
	return list
}

func (s *Set[T]) Equals(other *Set[T]) bool {
	// Check if both sets are nil
	if s == nil && other == nil {
		return true
	}

	// Check if one set is nil while the other is not
	if s == nil || other == nil {
		return false
	}

	// Check if the sets have the same number of elements
	if len(s.elements) != len(other.elements) {
		return false
	}

	// Check if all elements in s are in other
	for elem := range s.elements {
		if _, exists := other.elements[elem]; !exists {
			return false
		}
	}

	return true
}
