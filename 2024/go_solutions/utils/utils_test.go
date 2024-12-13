package utils

import (
	"os"
	"reflect"
	"testing"
)

func TestReadInputFile(t *testing.T) {
	tmpfile, err := os.CreateTemp("", "example")
	if err != nil {
		t.Fatalf("failed to create temp file: %s", err)
	}
	defer os.Remove(tmpfile.Name())

	content := "Hello, World"
	if _, err := tmpfile.WriteString(content); err != nil {
		t.Fatalf("failed to write to temp file: %s", err)
	}

	if err := tmpfile.Close(); err != nil {
		t.Fatalf("failed to close temp file: %s", err)
	}

	result := ReadInputFile(tmpfile.Name())
	if result != content {
		t.Errorf("expected %q, got %q", content, result)
	}
}

func TestCount(t *testing.T) {
	list := []int{1, 2, 3, 4, 5, 3, 1, 5}
	target := 3
	occurence := Count(list, target)
	if occurence != 2 {
		t.Errorf("expected %q, got %q", 2, occurence)
	}
}

func TestAbs(t *testing.T) {
	diff := Abs(1 - 3)
	if diff != 2 {
		t.Errorf("expected %q, got %q", 2, diff)
	}

	diff = Abs(3 - 1)
	if diff != 2 {
		t.Errorf("expected %q, got %q", 2, diff)
	}
	if Abs(0) != 0 {
		t.Errorf("expected %q, got %q", 0, Abs(0))
	}
}

func TestFilter(t *testing.T) {
	numbers := []int{1, 2, 3, 4, 5}
	filtered_numbers := Filter(numbers, func(n int) bool {
		return n%2 == 0
	})
	expected := []int{2, 4}
	if !reflect.DeepEqual(expected, filtered_numbers) {
		t.Errorf("expected %v, got %v", expected, filtered_numbers)
	}
}

func TestSetAdd(t *testing.T) {
	intSet := NewSet[int]()
	list := []int{1, 2, 3, 4, 5, 3, 1, 5}
	for _, element := range list {
		intSet.Add(element)
	}
	t.Log(intSet)

	target := 5
	size := intSet.Size()
	if size != target {
		t.Errorf("expected %d, got %d", target, size)
	}
}

func TestSetRemove(t *testing.T) {
	intSet := NewSet[int]()
	list := []int{1, 2, 3, 4, 5, 3, 1, 5}
	for _, element := range list {
		intSet.Add(element)
	}
	t.Log(intSet)

	intSet.Remove(2)
	t.Log(intSet)

	if intSet.Contains(2) {
		t.Errorf("expected set not to contain element after removal")
	}
}

func TestPopBack(t *testing.T) {
	list := []int{1, 2, 3, 4, 5, 3, 1, 5}
	expected_pop, expected_slice := 5, []int{1, 2, 3, 4, 5, 3, 1}

	popped, canPop := PopBack(&list)

	if !canPop || expected_pop != popped {
		t.Errorf("expected %d, got %d", expected_pop, popped)
	}

	if len(list) != len(expected_slice) {
		t.Errorf("expected %d, got %d", len(expected_slice), len(list))
	}
}

func TestQueue(t *testing.T) {
	q := NewQueue[int]()

	is_empty := q.IsEmpty()
	expected_true := true
	if is_empty != expected_true {
		t.Errorf("expected %t, got %t", expected_true, is_empty)
	}

	q.Enqueue(3)
	expected := 1
	if q.Size() != expected {
		t.Errorf("expected %d, got %d", expected, q.Size())
	}

	item, _ := q.Dequeue()
	expected = 3
	if item != expected {
		t.Errorf("expected %d, got %d", expected, item)
	}

	_, status := q.Dequeue()
	expected_false := false
	if status != expected_false {
		t.Errorf("expected %t, got %t", expected_false, status)
	}
}

func TestList(t *testing.T) {
	q := NewList[int]()

	q.Add(10)
	expected := 1

	if q.Size() != expected {
		t.Errorf("expected %d, got %d", expected, q.Size())
	}

	q.Add(3)
	expected = 10
	current := q.head
	if current.value != expected {
		t.Errorf("expected %d, got %d", expected, current.value)
	}

	expectedNext := 3
	current = current.next
	if current.value != expectedNext {
		t.Errorf("expected %d, got %d", expected, current.value)
	}

	canRemove := q.Remove(10)
	expected_true := true
	if canRemove != expected_true {
		t.Errorf("expected %t, got %t", expected_true, canRemove)
	}

}
