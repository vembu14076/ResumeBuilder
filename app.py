from flask import Flask, render_template, request

app = Flask(__name__)

# FORM PAGE (UI page)
@app.route("/", methods=["GET"])
def form():
    return render_template("form.html")


# RESUME GENERATE PAGE
@app.route("/generate", methods=["POST"])
def generate():
    data = {
        "name": request.form.get("name"),
        "phone": request.form.get("phone"),
        "email": request.form.get("email"),
        "location": request.form.get("location"),
        "about": request.form.get("about"),
        "education": request.form.get("education"),
        "skills": request.form.get("skills"),
        "projects": request.form.get("projects"),
        "experience": request.form.get("experience"),
        "hobbies": request.form.get("hobbies"),
        "languages": request.form.get("languages"),
        "linkedin": request.form.get("linkedin")
    }

    return render_template("resume.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)