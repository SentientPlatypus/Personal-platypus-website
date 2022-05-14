from flask import Flask,render_template, request, session, redirect, url_for
import smtplib, ssl
from threading import Thread
import csv
context = ssl.create_default_context()


class constants():
    EMAILREGEX            = '\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    EMAIL                 = "trexxxxxxxxxxy@gmail.com"
    EMAILPASSWORD         = "toltlbokcaiicooy"
    PORT                  = 465  # For SSL

#path = '/home/SentientPlatypus/Personal-platypus-website/code'
#if path not in sys.path:
#    sys.path.append(path)

#from services.main import app as application

def createApp():
    app = Flask(
    __name__,
    template_folder=r"templates",
    static_folder=r"static"
    )
    return app

app = createApp()

@app.route("/")
def home():
    return render_template("./index.html")

@app.route("/index")
def home1():
    return render_template("./index.html")

@app.route("/discord")
def discord():
    return render_template("./discord.html")

@app.route("/products")
def products():
    return render_template("./products.html")

@app.route("/projects")
def projects():
    return render_template("./projects.html")

@app.route("/papers")
def papers():
    return render_template("./papers.html")


@app.route("/inProgress")
def inProgress():
    return render_template("./inProgress.html")


@app.route("/ContactMe/<int:sent>")
def ContactMe(sent):
    bool = False
    if sent == 1:
        bool = True
    return render_template("./index.html", sent=bool)

@app.route("/gaming")
def gaming():
    return render_template("./gaming.html")


@app.route("/resume")
def resume():
    return render_template("./underConstruction.html")


@app.route("/socials")
def socials():
    return render_template("./socials.html")

@app.route("/exercise")
def exercise():
    return render_template("./exercise.html")


@app.route("/underConstruction")
def underConstruction():
    return render_template("./underConstruction.html")

    
@app.route("/ContactMe/HandleData", methods=['POST'])
def HandleData():
    projectpath = request.form    
    sendingEmail = projectpath.get("email")
    name = projectpath.get("name")
    subject = projectpath.get("subject")
    message = projectpath.get("content")
    gmail_user = constants.EMAIL
    gmail_password = constants.EMAILPASSWORD
    to = [constants.EMAIL]
    email_text = """
    From: %s , %s
    To: %s
    Subject: %s

    %s
    """ % (sendingEmail,name, ", ".join(to), subject, message)
    print(email_text)
    try:
        print("working")
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        print("checkpoint19")
        smtp_server.ehlo()
        print("checkpoint20")
        smtp_server.login(gmail_user, gmail_password)
        print("done logging in")
        smtp_server.sendmail(sendingEmail, to, email_text)
        smtp_server.close()
        print ("Email sent successfully!")
    except Exception as ex:
        print ("Something went wrong….", ex)
    return redirect(url_for("ContactMe", sent=1))


def run():
  app.run(host='0.0.0.0',port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()


if __name__ == '__main__':
    keep_alive()

