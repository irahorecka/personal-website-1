from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    title = "Home Page"
    return render_template("home.html", title=title)

@app.route("/about")
def about():
    title = "About"
    return render_template("about.html", title=title)

@app.route("/projects")
def coding_projects():
    title = "Coding Projects"
    return render_template("projects.html", title=title)

@app.route("/astree")
def astree():
    title = "ASTree"
    return render_template("astree.html", title=title)

@app.route("/actransit")
def actransit():
    title = "AC Transit"
    return render_template("actransit.html", title=title)

@app.route("/craigslistmining")
def cl_mining():
    title = "Craigslist Mining"
    return render_template("craigslistmining.html", title=title)

@app.route("/visuaudio")
def visuaudio():
    title = "Visualize Audio"
    return render_template("visuaudio.html", title=title)

@app.route("/youtube2audio")
def youtube2audio():
    title = "YouTube to Audio"
    return render_template("youtube2audio.html", title=title)


if __name__ == "__main__":
    app.run(debug=True)
