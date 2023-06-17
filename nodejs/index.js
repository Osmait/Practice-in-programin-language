const fs = require("fs");

// fetch("https://dummyjson.com/products/1")
//   .then((r) => r.json())
//   .then((r) => fs.writeFileSync("product.json", JSON.stringify(r)));

// const result = fs.readFileSync("product.json", "utf8");

// console.log(JSON.parse(result));

const response = await fetch("https://dummyjson.com/products/1");
const data = await response.json();
console.log(data);
