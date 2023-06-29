mod dataStructure;
mod leetcode;
mod sort;
mod utils;
use crate::leetcode::contain_duplicate;
use crate::leetcode::is_anagram;
use std::fs;

fn main() {
    let mut queue = dataStructure::queue::Queue::<i32>::new();
    queue.enqueu(1);
    queue.enqueu(2);
    queue.enqueu(3);
    println!("{:?}", queue);
    let mut res = vec![10, 8, 4, 3, 1, 9, 2, 7, 5, 6];
    sort::quick_sort::quick_sort(&mut res);
    println!("{:?}", res);
    match utils::fetch::fetch() {
        Ok(products) => println!("{:?}", products),
        Err(error) => println!("{}", error),
    }

    let s = String::from("anagram");
    let t = String::from("nagaram");
    let result = contain_duplicate::contain_duplicate(vec![1, 2, 3, 1]);
    let result2 = is_anagram::is_anagram(s, t);
    println!("{}", result2);
    println!("{}", result);
    let multiplication = |x: i64| -> i64 { x * x };

    println!("{}", multiplication(5));

    let file = fs::read_to_string("prueba.txt");
    match file {
        Ok(f) => println!("{}", f),
        Err(e) => eprintln!("{}", e),
    }
    let r = calculate(10, 20);
    let range = 10..=20;
    range.for_each(|x| println!("{}", x));

    println!("{}", r);
}

fn calculate(bottom: i32, top: i32) -> i32 {
    (bottom..=top).filter(|x| x % 2 == 0).sum()
}
