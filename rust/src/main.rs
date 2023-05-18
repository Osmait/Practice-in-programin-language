fn main() {
    // let sauldo: &str = "Hello, world!";
    let name = String::from("hola");
    print!("{}", say_my_name(name))
}

fn say_my_name(name: String) -> String {
    return format!("my nombre es {}\n", name);
}
