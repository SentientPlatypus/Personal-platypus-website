from flask import Flask,render_template, request, session, redirect, url_for
import smtplib, ssl
import constants
import csv
context = ssl.create_default_context()

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


@app.route("/underConstruction")
def underConstruction():
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

    # with open("./contacts.csv", "a") as f:
    #     csvWriter = csv.writer(f)
    #     csvWriter.writerow([name, sendingEmail, subject, message])
    gmail_user = constants.EMAIL
    gmail_password = constants.EMAILPASSWORD
    to = [constants.EMAIL]
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

