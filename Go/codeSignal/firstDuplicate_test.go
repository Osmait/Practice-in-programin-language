package codesignal

import "testing"

func TestFirstDuplicate(t *testing.T) {
	type args struct {
		a []int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "prueba",
			args: args{
				a: []int{2, 1, 3, 5, 3, 2},
			},
			want: 3,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := FirstDuplicate(tt.args.a); got != tt.want {
				t.Errorf("FirstDuplicate() = %v, want %v", got, tt.want)
			}
		})
	}
}
