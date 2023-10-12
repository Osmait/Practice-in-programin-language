package codewars

import (
	"testing"
)

func TestSolution(t *testing.T) {

	result := name_shuffler("saul Burgos")
	expecte := "Burgos saul"
	if expecte != result {
		t.Errorf("Error expected %s but got %s", expecte, result)
	}
}

func TestFirstNonconsecutiv(t *testing.T) {
	result := FirstNonConsecutiv([]int{1, 2, 3, 4, 6, 7, 8})

	expect := 6
	if expect != *result {
		t.Errorf("Error expected %d but got %d", expect, result)
	}
}
