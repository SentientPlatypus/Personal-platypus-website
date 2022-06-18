#[macro_use] extern crate rocket;




#[get("/")]
fn index() -> &'static str {
    "Hello world"
}

#[get("/words")]
fn words() -> &'static str
{
    "Hello words!"
}






#[launch]
fn rocket() -> _ {
    rocket::build()
    .mount("/", routes![index, words])
    .mount("/words", routes![words])    
}