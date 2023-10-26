const numbers = [1, 2, 3, 4, 5, 6];

// Método .push() - Agregar elementos al final del array
numbers.push(7, 8);
console.log(numbers); // [1, 2, 3, 4, 5, 6, 7, 8]

// Método .pop() - Eliminar el último elemento del array
const lastNumber = numbers.pop();
console.log(lastNumber); // 8
console.log(numbers); // [1, 2, 3, 4, 5, 6, 7]

// Método .shift() - Eliminar el primer elemento del array
const firstNumber = numbers.shift();
console.log(firstNumber); // 1
console.log(numbers); // [2, 3, 4, 5, 6, 7]

// Método .unshift() - Agregar elementos al principio del array
numbers.unshift(0, 1);
console.log(numbers); // [0, 1, 2, 3, 4, 5, 6, 7]

// Método .concat() - Concatenar arrays
const moreNumbers = [8, 9, 10];
const combinedNumbers = numbers.concat(moreNumbers);
console.log(combinedNumbers); // [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

// Método .slice() - Extraer una porción del array
const slicedNumbers = combinedNumbers.slice(3, 7);
console.log(slicedNumbers); // [3, 4, 5, 6]

// Método .splice() - Modificar el contenido del array
combinedNumbers.splice(3, 4, 11, 12, 13);
console.log(combinedNumbers); // [0, 1, 2, 11, 12, 13, 7, 8, 9, 10]

// Método .filter() - Crear un nuevo array con elementos que cumplan una condición
const evenNumbers = combinedNumbers.filter((number) => number % 2 === 0);
console.log(evenNumbers); // [0, 2, 12]

// Método .map() - Crear un nuevo array aplicando una función a cada elemento
const squaredNumbers = combinedNumbers.map((number) => number * number);
console.log(squaredNumbers); // [0, 1, 4, 121, 144, 169, 49, 64, 81, 100]

// Método .reduce() - Reducir el array a un valor único mediante una función acumuladora
const sum = combinedNumbers.reduce((accumulator, currentValue) => accumulator + currentValue, 0);
console.log(sum); // 615

// Método .sort() - Ordenar el array
const sortedNumbers = combinedNumbers.slice().sort((a, b) => a - b);
console.log(sortedNumbers);

// Método .forEach() - Realizar una operación en cada elemento del array
combinedNumbers.forEach((number) => {
  console.log(number);
});


// Método .every() - Verificar si todos los elementos cumplen una condición
const allEven = numbers.every((number) => number % 2 === 0);
console.log(allEven); // false

// Método .some() - Verificar si al menos un elemento cumple una condición
const hasEven = numbers.some((number) => number % 2 === 0);
console.log(hasEven); // true

// Método .find() - Encontrar el primer elemento que cumple una condición
const firstEven = numbers.find((number) => number % 2 === 0);
console.log(firstEven); // 2

// Método .findIndex() - Encontrar el índice del primer elemento que cumple una condición
const firstEvenIndex = numbers.findIndex((number) => number % 2 === 0);
console.log(firstEvenIndex); // 1

// Método .includes() - Verificar si un valor está presente en el array
const includesThree = numbers.includes(3);
console.log(includesThree); // true


// Clonar un array
const originalArray = [1, 2, 3];
const clonedArray = [...originalArray];
console.log(clonedArray); // [1, 2, 3]
console.log(originalArray === clonedArray); // false (no son la misma referencia)

// Combinar varios arrays
const array1 = [1, 2];
const array2 = [3, 4];
const combinedArray = [...array1, ...array2];
console.log(combinedArray); // [1, 2, 3, 4]

// Agregar elementos a un array
const initialArray = [1, 2, 3];
const newArray = [...initialArray, 4, 5];
console.log(newArray); // [1, 2, 3, 4, 5]

// Copiar y modificar elementos de un array

const modifiedNumbers = [...numbers.slice(0, 1), 4, ...numbers.slice(2)];
console.log(modifiedNumbers); // [1, 4, 3]

// Desestructurar un array
const [first, ...rest] = [1, 2, 3, 4];
console.log(first); // 1
console.log(rest); // [2, 3, 4]

// Convertir una cadena en un array de caracteres
const str = "hello";
const charArray = [...str];
console.log(charArray); // ["h", "e", "l", "l", "o"]la misma referencia)
