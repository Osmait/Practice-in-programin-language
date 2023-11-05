package codesignal

import "testing"

func TestFirstNotRepeating(t *testing.T) {
	type args struct {
		s string
	}
	tests := []struct {
		name string
		args args
		want string
	}{
		{
			name: "Test1",
			args: args{s: "abacabad"},
			want: "c",
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := FirstNotRepeating(tt.args.s); got != tt.want {
				t.Errorf("FirstNotRepeating() = %v, want %v", got, tt.want)
			}
		})
	}
}
