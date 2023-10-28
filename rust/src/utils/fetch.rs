extern crate reqwest;

pub async fn fetch(url: String) {
    let response = reqwest::get(url).await.unwrap();

    let body = response.text().await.unwrap();
    println!("{}", body)
}
