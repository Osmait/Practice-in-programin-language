mod leetcode;

use std::fs;

use crate::leetcode::contain_duplicate;
use crate::leetcode::is_anagram;

struct Pair(Box<i32>, Box<i32>);

fn main() {
    let s = String::from("anagram");
    let t = String::from("nagaram");
    let result = contain_duplicate::contain_duplicate(vec![1, 2, 3, 1]);
    let result2 = is_anagram::is_anagram(s, t);
    println!("{}", result2);
    println!("{}", result);
    let multiplication = |x: i64| -> i64 { x * x };

    println!("{}", multiplication(5));

    let a = Box::new(5);
    let b = Box::new(10);
    let pair = Pair(a, b);

    // Acceder a los valores dentro de la estructura Pair
    let value1 = *pair.0;
    let value2 = *pair.1;

    println!("Valor 1: {}", value1);
    println!("Valor 2: {}", value2);
    let r = value1 + value2;
    println!("{}", r);

    let file = fs::read_to_string("prueba.txt");
    match file {
        Ok(f) => println!("{}", f),
        Err(e) => eprintln!("{}", e),
    }
}
