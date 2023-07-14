import fs from "node:fs/promises";

interface Product {
  id: number;
  title: string;
  description: string;
  price: number;
}

async function Main() {
  await fetch("https://dummyjson.com/products/1")
    .then((r) => r.json())
    .then((r) => fs.writeFile("product.json", JSON.stringify(r)));

  const result = await fs.readFile("product.json", "utf8");
  const product: Product = JSON.parse(result);
  console.log(product);
}
Main();

// "id": 1,
// "title": "iPhone 9",
// "description": "An apple mobile which is nothing like apple",
// "price": 549,
