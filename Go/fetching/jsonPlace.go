package fetching

import (
	"encoding/json"
	"fmt"
	"net/http"
)

type User struct {
	UseId     int    `json:"userId"`
	Id        int    `json:"id"`
	Title     string `json:"title"`
	Completed bool   `json:"completed"`
}

func (u *User) ToString() string {
	return fmt.Sprintf("UserId: %d, Id: %d, Title: %s, Completed: %t", u.UseId, u.Id, u.Title, u.Completed)
}

func Fetch(url string) (*User, error) {

	var user User
	rep, err := http.Get(url)

	json.NewDecoder(rep.Body).Decode(&user)

	if err != nil {
		return nil, err
	}
	defer rep.Body.Close()

	return &user, nil

}
