import os
from pathlib import Path
from flask import render_template, url_for
from personalWebsite import app


@app.route("/")
@app.route("/home")
def home():
    title = "Ira Horecka"
    return render_template("home.html", title=title)


@app.route("/about")
def about():
    title = "About"
    text_body = parse_textfile("about.txt")
    return render_template("about.html", title=title, texts=text_body)


@app.route("/bikes")
def bikes():
    title = "Bike Gallery"
    img_folder = "super-sport"
    content = {
        "bike": "1972 Schwinn Super Sport",
        "image_folder": img_folder,
        "images": get_bike_images(img_folder)
    }
    return render_template("bikes.html", title=title, content=content)


@app.route("/projects")
def coding_projects():
    title = "Coding Projects"
    return render_template("projects.html", title=title)


@app.route("/projects/astree")
def astree():
    title = "ASTree"
    return render_template("astree.html", title=title)


@app.route("/projects/actransit")
def actransit():
    title = "AC Transit"
    text_body = parse_textfile("actransit.txt")
    return render_template("actransit.html", title=title, texts=text_body)


@app.route("/projects/craigslist-mining")
def cl_mining():
    title = "Craigslist Mining"
    return render_template("craigslistmining.html", title=title)


@app.route("/projects/visuaudio")
def visuaudio():
    title = "Visualize Audio"
    text_body = parse_textfile("visuaudio.txt")
    return render_template("visuaudio.html", title=title, texts=text_body)


@app.route("/projects/youtube2audio")
def youtube2audio():
    title = "YouTube to Audio"
    text_body = parse_textfile("youtube2audio.txt")
    return render_template("youtube2audio.html", title=title, texts=text_body)


@app.errorhandler(404)
def not_found(e):
    """Page not found."""
    return render_template("404.html"), 404


def parse_textfile(textfile_name):
    text_path = Path(__file__).parent / f"./text_body/{textfile_name}"
    with text_path.open() as text:
        texts = text.readlines()
    texts = [text.strip() for text in texts]

    return texts


def get_bike_images(bikefolder_name):
    bike_img_path = Path(__file__).parent / f"./static/bike_img/{bikefolder_name}"
    bike_imgs = [img for img in os.listdir(bike_img_path)]
    print(bike_imgs)

    return bike_imgs
