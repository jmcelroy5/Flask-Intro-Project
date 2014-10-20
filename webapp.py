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

    html = render_template("index.html", first_name = row[0],
                                        last_name = row[1],
                                        github = row[2],
                                        grades = grades)
    return html

@app.route('/project')
def list_project_grades():
   hackbright_app.connect_to_db()
   project_name = request.args.get("title") # Getting this key from the URL
   
   student_info = hackbright_app.show_all_grades(project_name)
   
   project_info = hackbright_app.get_project(project_name)

   project_title = project_info[1]
   description = project_info[2]
   max_grade = project_info[3]

   html = render_template("project.html", title = project_title,
                                        max_grade = max_grade,
                                        description = description,
                                        grades = student_info)
   return html


if __name__ == "__main__":
    app.run(debug=True)