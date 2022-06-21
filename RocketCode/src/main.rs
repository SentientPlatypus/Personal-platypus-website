#[macro_use] extern crate rocket;
use rocket::fs::{FileServer, relative};
use rocket::form::{Form, Contextual, FromForm, FromFormField, Context};
use rocket_dyn_templates::{Template, tera::Tera, context};


#[get("/")] 
fn main_page() -> Template {
    Template::render("index", &Context::default())
}

#[get("/socials")] 
fn socials() -> Template {
    Template::render("socials", &Context::default())
}

#[get("/gaming")] 
fn gaming() -> Template {
    Template::render("gaming", &Context::default())
}

#[get("/exercise")] 
fn exercise() -> Template {
    Template::render("exercise", &Context::default())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
    .mount("/", routes![main_page, socials, gaming, exercise]).attach(Template::fairing())
    .mount("/", FileServer::from(relative!("/static")))
}