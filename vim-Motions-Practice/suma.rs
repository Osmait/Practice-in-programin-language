fn main() {
    let string1 = String::from("long string is long");
    let result = suma(12, 21);
    println!("{}", result);
}

fn suma(a: i32, b: i32) -> i32 {
    return a + b;
}
fn resta(a: i32, b: i32) {
    return a - b;
}

fn multiply(a: i32, b: i32) {
    return a * b;
}
