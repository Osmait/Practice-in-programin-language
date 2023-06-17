// const result = fetch("https://dummyjson.com/products")
//   .then((response) => response.json())
//   .then((data) => data);

// result.then((data) => console.log(data));

const list = [1, 2, 3, 4];

console.log(list.reduce((a, b) => a + b, 0));

const listofPerson = [
  {
    name: "John",
  },
  {
    lastName: "Jane",
  },
];

const result = listofPerson.map((person) => Object.keys(person));

const [k, v] = Object.keys({
  lastName: "Jane",
});

console.log(result.flat());
