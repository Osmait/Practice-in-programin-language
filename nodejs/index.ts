import fs from "fs/promises";
import puppeteer from "puppeteer";

// fetch("https://dummyjson.com/products/1")
//   .then((r) => r.json())
//   .then((r) => fs.writeFileSync("product.json", JSON.stringify(r)));

// interface Product {
//   id: number;
//   title: string;
//   description: string;
//   price: number;
// }

async function Main() {
  //   const response = await fetch("https://dummyjson.com/products/1");
  //   const data = await response.json();
  //   //   console.log(data);
  //   const result = await fs.readFile("product.json", "utf8");
  //   const product: Product = JSON.parse(result);
  //   console.log(product);
  const browser = await puppeteer.launch({ headless: "new" });
  const page = await browser.newPage();
  await page.goto(
    "https://myanimelist.net/anime/5114/Fullmetal_Alchemist__Brotherhood"
  );

  const title = await page.waitForSelector("h1 > .title-name");
  console.log(title);

  await browser.close();
}
Main();

// "id": 1,
// "title": "iPhone 9",
// "description": "An apple mobile which is nothing like apple",
// "price": 549,
