from quart import Quart, render_template, request, session, redirect, url_for
from flask import Flask,render_template, request, session, redirect, url_for
import smtplib, ssl
emailRegex = '\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
password = "geneavianina"
port = 465  # For SSL
# Create a secure SSL context
context = ssl.create_default_context()




app = Flask(
    __name__,
    template_folder=r"C:\Users\trexx\Documents\PYTHON CODE LOL\PersonalWebsite\Personal-platypus-website\code\templates",
    static_folder=r"C:\Users\trexx\Documents\PYTHON CODE LOL\PersonalWebsite\Personal-platypus-website\code\static"
)


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

@app.route("/ContactMe/<int:sent>")
def ContactMe(sent):
    bool = False
    if sent == 1:
        bool = True
    return render_template("./ContactMe.html", sent=bool)

@app.route("/resume")
def resume():
    return render_template("./underConstruction.html")


@app.route("/ContactMe/HandleData", methods=['POST'])
def HandleData():
    projectpath = request.form
    print(projectpath)
    form = {}
    for key in projectpath.keys():
        values = projectpath.getlist(key)
        if len(values) == 1:
            form[key] = values[0]
        else:
            form[key] = values

    sendingEmail = form["email"]
    name = form["name"]
    subject = form["subject"]
    message = form["content"]


    gmail_user = 'geneustace.wicaksono@icsd.k12.ny.us'
    gmail_password = 'geneavianina'

    to = ['geneustace.wicaksono@icsd.k12.ny.us']

    email_text = """
    From: %s , %s
    To: %s
    Subject: %s

    %s
    """ % (sendingEmail,name, ", ".join(to), subject, message)
    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(sendingEmail, to, email_text)
        smtp_server.close()
        print ("Email sent successfully!")
    except Exception as ex:
        print ("Something went wrong….",ex)
    return redirect(url_for("ContactMe", sent=1))

if __name__ == '__main__':
    app.run(
        debug=True,
        port=80,
        )

