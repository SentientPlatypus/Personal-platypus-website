#[macro_use] extern crate rocket;
use rocket::fs::{FileServer, relative};
use rocket::http::{Status, ContentType};
use rocket::form::{Form, Contextual, FromForm, FromFormField, Context};
use rocket_dyn_templates::{Template, tera::Tera, context};
use lettre_email::EmailBuilder;
use lettre::smtp::authentication::Credentials;
use lettre::{SmtpClient, Transport};



fn get_email() -> String {
    String::from("trexxxxxxxxxxy@gmail.com")
}

fn get_password() -> String {
    String::from("YEAH NOPE LOL")
}







#[derive(Debug, FromForm)]
struct Submission
{
    name: String,
    #[field(validate = contains('@').or_else(msg!("invalid email address")))]
    email: String,
    subject: String,
    content: String,
}



#[get("/")] 
fn main_page() -> Template {
    Template::render("index", context!{})
}

#[get("/socials")] 
fn socials() -> Template {
    Template::render("socials", context!{})
}

#[get("/gaming")] 
fn gaming() -> Template {
    Template::render("gaming", context!{})
}

#[get("/exercise")] 
fn exercise() -> Template {
    Template::render("exercise", context!{})
}

#[post("/", data = "<form>")]
fn submit(form:Form<Contextual<Submission>>) -> Template {
    match &form.value {
        Some(submission) => {
            let sending_email = get_email();
            let sending_email_pass = get_password();
            println!("{:#?}", submission);
            let email = EmailBuilder::new()
                .to(("geneustace.wicaksono@icsd.k12.ny.us", "Gene W"))
                .from((&sending_email, &submission.name))
                .subject(&submission.subject)
                .text(&submission.content)
                .build();
            match email {
                Ok(success_email) => {
                    let mailer = SmtpClient::new_simple("smtp.googlemail.com");
                    match mailer {
                        Ok(new_mailer) => {
                            let mut transport = new_mailer
                                .credentials(Credentials::new(sending_email.into(), sending_email_pass.into()))
                                .transport();
                            match transport.send(success_email.into()) {
                                Ok(_) => println!("Success!"),
                                Err(er) => println!("{}", er)
                            }
                        }   
                        Err(er) => {
                            println!("{}", er);
                        }
                    }
                },
                Err(er) => {
                    println!("{}", er)
                }
            };
            return Template::render("index", context!{})
        }
        None => Template::render("index", context!{})
    }
}

#[launch]
fn rocket() -> _ {
    rocket::build()
    .mount("/", routes![main_page, socials, gaming, exercise, submit]).attach(Template::fairing())
    .mount("/", FileServer::from(relative!("/static")))
}