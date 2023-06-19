mod leetcode;
mod sort;

// use std::fs;

use std::fmt;

// use crate::leetcode::contain_duplicate;
// use crate::leetcode::is_anagram;
use reqwest::Error;
// struct Pair(Box<i32>, Box<i32>);
use serde::Deserialize;

#[derive(Debug, Deserialize)]
struct Products {
    id: i32,
    title: String,
    description: String,
    price: f32,
}

impl fmt::Display for Products {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(
            f,
            "id:{},\ntitle: {},\ndescription: {},\nprice:{}",
            self.id, self.title, self.description, self.price
        )
    }
}

#[tokio::main]
async fn main() -> Result<(), Error> {
    let mut res = vec![10, 8, 4, 3, 1, 9, 2, 7, 5, 6];
    sort::merger_sort::top_down_merge_sort(&mut res);
    println!("{:?}", res);

    // let s = String::from("anagram");
    // let t = String::from("nagaram");
    // let result = contain_duplicate::contain_duplicate(vec![1, 2, 3, 1]);
    // let result2 = is_anagram::is_anagram(s, t);
    // println!("{}", result2);
    // println!("{}", result);
    // let multiplication = |x: i64| -> i64 { x * x };

    // println!("{}", multiplication(5));

    // let a = Box::new(5);
    // let b = Box::new(10);
    // let pair = Pair(a, b);

    // // Acceder a los valores dentro de la estructura Pair
    // let value1 = *pair.0;
    // let value2 = *pair.1;

    // println!("Valor 1: {}", value1);
    // println!("Valor 2: {}", value2);
    // let r = value1 + value2;
    // println!("{}", r);

    // let file = fs::read_to_string("prueba.txt");
    // match file {
    //     Ok(f) => println!("{}", f),
    //     Err(e) => eprintln!("{}", e),
    // }
    let r = calculate(10, 20);
    let range = 10..=20;
    range.for_each(|x| println!("{}", x));

    println!("{}", r);

    let response = reqwest::get("https://dummyjson.com/products/1").await?;

    if response.status().is_success() {
        let body = response.text().await?;
        let products: Products = serde_json::from_str(&body).unwrap();

        println!("{}", products);
    } else {
        println!("La petición no fue exitosa: {}", response.status());
    }

    Ok(())
}

fn calculate(bottom: i32, top: i32) -> i32 {
    (bottom..=top).filter(|x| x % 2 == 0).sum()
}
