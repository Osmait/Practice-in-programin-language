package repository

type Repository interface {
	Save(dato string)
	Find() []string
}

type ImplRepository struct {
	list []string
}

func New() *ImplRepository {
	return &ImplRepository{}
}

func (r *ImplRepository) Save(dato string) {
	r.list = append(r.list, dato)
}

func (r *ImplRepository) Find() []string {
	return r.list
}
