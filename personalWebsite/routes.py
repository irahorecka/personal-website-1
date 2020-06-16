import os
import json
from pathlib import Path
from flask import render_template, request, url_for
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


@app.route("/projects")
def coding_projects():
    title = "Coding Projects"
    content = get_project_json()
    projects = content["projects"]
    content["projects"] = sorted(
        projects, key=lambda x: len(str(x["title"])), reverse=True
    )

    return render_template("projects.html", title=title, content=content)


@app.route("/projects/<project_id>")
def indiv_project(project_id):
    current_project = get_current_json_obj("projects", project_id)
    title = current_project["title"]
    text_body = parse_textfile(f"projects/{project_id}.txt")

    return render_template(
        "project.html", title=title, texts=text_body, content=current_project
    )


@app.route("/bikes")
def bikes():
    title = "Bike Gallery"
    content = get_bike_json()
    bikes = content["bikes"]
    # sort bike gallery content by text length
    content["bikes"] = sorted(
        bikes, key=lambda x: len(str(x["year"]) + x["make"] + x["model"]), reverse=True
    )
    return render_template("bikes.html", title=title, content=content)


@app.route("/bikes/<bike_id>")
def indiv_bike(bike_id):
    current_bike = get_current_json_obj("bikes", bike_id)
    title = f"{current_bike['year']} {current_bike['make']} {current_bike['model']}"
    text_body = parse_textfile(f"bikes/{bike_id}.txt")
    # allow six images for every individual bike page.
    img_keys = ["<img_1>", "<img_2>", "<img_3>", "<img_4>", "<img_5>", "<img_6>"]

    return render_template(
        "bike.html",
        title=title,
        texts=text_body,
        content=current_bike,
        img_keys=img_keys,
    )


@app.errorhandler(404)
def not_found(e):
    """Page not found."""
    return render_template("error/404.html"), 404


def get_current_json_obj(json_key, json_endpoint):
    keys = {
        "bikes": get_bike_json()["bikes"],
        "projects": get_project_json()["projects"],
    }
    current_item = keys[json_key]
    content = None
    for item in current_item:
        if item["endpoint"] == json_endpoint:
            content = item
    if not content:
        return render_template("error/404.html"), 404

    return content


def parse_textfile(textfile_name):
    text_path = Path(__file__).parent / f"./text_body/{textfile_name}"
    with text_path.open() as text:
        texts = text.readlines()
    texts = [text.strip() for text in texts]

    return texts


def get_project_json():
    project_json_path = Path(__file__).parent / f"./static/projects.json"
    with open(project_json_path) as project_json:
        data = json.load(project_json)

    return data


def get_bike_json():
    bike_json_path = Path(__file__).parent / f"./static/bikes.json"
    with open(bike_json_path) as bike_json:
        data = json.load(bike_json)

    return data
