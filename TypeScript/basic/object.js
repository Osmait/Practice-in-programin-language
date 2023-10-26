// Creación de objetos// Creación de objetos
const person = {
  name: 'John',
  age: 30,
};

const car = new Object();
car.make = 'Toyota';
car.model = 'Camry';

// Acceso y modificación de propiedades
person.name; // Acceder a una propiedad
person.age = 31; // Modificar una propiedad

car['make']; // Acceder a una propiedad
car['model'] = 'Corolla'; // Modificar una propiedad

// Eliminación de propiedades
delete person.age; // Eliminar una propiedad

// Iteración sobre propiedades
for (const key in person) {
  console.log(key, person[key]);
}

// Métodos para objetos incorporados
const keys = Object.keys(person); // Devuelve un array de las claves del objeto
const values = Object.values(person); // Devuelve un array de los valores del objeto
const entries = Object.entries(person); // Devuelve un array de arrays [clave, valor]

// Clonación y fusión de objetos
const clonePerson = { ...person }; // Clonar un objeto
const mergedObject = Object.assign({}, person, car); // Combinar objetos en uno

// Verificación de propiedades
person.hasOwnProperty('name'); // Comprobar si el objeto tiene la propiedad 'name'

// Definición de propiedades con atributos específicos
Object.defineProperty(person, 'gender', {
  value: 'male',
  writable: false, // Propiedad no modificable
  enumerable: true, // Se enumera al iterar
});

// Congelar objetos
Object.freeze(person); // Hace que el objeto 'person' sea inmutable
