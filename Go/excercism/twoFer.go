package excercism

import "fmt"

func ShareWith(name string) string {
	// Write some code here to pass the test suite.
	// Then remove all the stock comments.
	// They're here to help you get started but they only clutter a finished solution.
	// If you leave them in, reviewers may protest!
	if name != "" {
		return fmt.Sprintf("One for %s, one for me.", name)
	}
	return "One for you, one for me."
}
