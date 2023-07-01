mod data_structure;
mod desing_patters;
mod leetcode;
mod sort;
use crate::desing_patters::repository;
use crate::desing_patters::repository::UserRepository;
// mod utils;
use crate::leetcode::contain_duplicate;
use crate::leetcode::is_anagram;
use std::fs;

fn main() {
    let mut list = data_structure::linked_list::LinkedList::<i32>::new();
    list.insert_at_head(1);
    list.insert_at_ith(1, 2);

    println!("{:?}", list);

    let mut repository1 = repository::ImplRepository::new();
    let dato = String::from("hola");
    let dato2 = String::from("prueba");
    repository1.save(dato2);
    repository1.save(dato);
    let mut queue = data_structure::queue::Queue::<i32>::new();
    let list = repository1.find();
    println!("{:?}", list);
    queue.enqueu(1);
    queue.enqueu(2);
    queue.enqueu(3);
    println!("{:?}", queue);
    let mut res = vec![10, 8, 4, 3, 1, 9, 2, 7, 5, 6];
    sort::merger_sort::top_down_merge_sort(&mut res);
    println!("{:?}", res);
    // match utils::fetch::fetch() {
    //     Ok(products) => println!("{:?}", products),
    //     Err(error) => println!("{}", error),
    // }
    //
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
