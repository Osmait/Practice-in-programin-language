use serde_json::Result;
use std::collections::HashMap;
mod codeWars;
mod code_signals;
mod data_structure;
mod desing_patters;
mod leetcode;
mod sort;
mod utils;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let resp = reqwest::get("https://httpbin.org/ip")
        .await?
        .json::<HashMap<String, String>>()
        .await?;
    println!("{:#?}", resp);
    Ok(())
}

fn calculate(bottom: i32, top: i32) -> i32 {
    (bottom..=top).filter(|x| x % 2 == 0).sum()
}
