from quart import Quart, render_template, request, session, redirect, url_for
from pymongo import MongoClient
import re

app = Quart(
    __name__,
    template_folder="C:\Users\trexx\Documents\PYTHON CODE LOL\PersonalWebsite\code\templates",
    static_folder="C:\Users\trexx\Documents\PYTHON CODE LOL\PersonalWebsite\code\static"
)


@app.route("/")
async def home():
    return await render_template("./index.html")