import hackbright_app
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def get_github():
    return render_template("get_github.html")

@app.route("/student")
def get_student():
    hackbright_app.connect_to_db()
    student_github = request.args.get("github")
    row = hackbright_app.get_student_by_github(student_github)
    first_name = row[0]
    last_name = row[1]

    grades = hackbright_app.show_grades(first_name,last_name)
    print grades
    # project_names, grades = zip(*grades)

    html = render_template("index.html", first_name = row[0],
                                        last_name = row[1],
                                        github = row[2],
                                        grades = grades
                                        # project_names = project_names
                                        )


# def list_project_grades():
#     hackbright_app



    return html

if __name__ == "__main__":
    app.run(debug=True)