from flask import Flask,render_template,redirect,request,url_for,flash,session
App=Flask(__name__)
App.secret_key="nisha"
student_list=[]
@App.route("/")
def index():
    return render_template("index.html")

@App.route("/login",methods=["GET","POST"])
def login():
    name="navin"
    password="12345"
    if request.method == "POST":
        Name=request.form.get("name")
        Password=request.form.get("password")
        if name == Name and password==Password:
            session["name"]=Name
            print("Session set:",session)
            return redirect(url_for("Home"))
        else:
            flash("Check User Name And Password")
            return redirect(url_for("login"))
        
    return render_template("login.html")

@App.route("/home")
def Home():
    if "name" not in session:
        flash("you need to login first","warning")
        return redirect(url_for("login"))
    return render_template("home.html",data=student_list)

@App.route("/addstudent",methods=["GET","POST"])
def Add():
    if request.method == "POST":
        Name=request.form.get("Name")
        Age=request.form.get("Age")
        RollNo=request.form.get("RollNo")
        Marktamil=request.form.get("Marktamil")
        Markenglish=request.form.get("Markenglish")
        Markmaths=request.form.get("Markmaths")
        Markscience=request.form.get("Markscience")
        Marksocial=request.form.get("Marksocialscience")
        mark_list=list()
        mark_list.append(int(Marktamil))
        mark_list.append(int(Markenglish))
        mark_list.append(int(Markmaths))
        mark_list.append(int(Markscience))
        mark_list.append(int(Marksocial))
        student_dict={}
        student_dict.update({"Name":Name})
        student_dict.update({"Age":Age})
        student_dict.update({"RollNO":RollNo})
        student_dict.update({"Marks":mark_list})
        student_list.append(student_dict)
        return redirect(url_for("Home"))
    return render_template("add.html")

@App.route("/delete/<int:index>",methods=["GET","POST"])
def delete(index):
    student_list.pop(int(index-1))
    return render_template("home.html",data=student_list)

@App.route("/edit/<int:index>",methods=["GET","POST"])
def edit(index):
    if request.method == "POST":
        edit_name=request.form.get("Name")
        edit_age=request.form.get("Age")
        edit_rollno=request.form.get("RollNo")
        edittamil=request.form.get("Marktamil")
        editenglish=request.form.get("Markenglish")
        editmaths=request.form.get("Markmaths")
        editscience=request.form.get("Markscience")
        editsocial=request.form.get("Marksocialscience")
        edit_mark=[edittamil,editenglish,editmaths,editscience,editsocial]
        student=student_list[int(index-1)]
        student.update({"Name":edit_name})
        student.update({"Age":edit_age})
        student.update({"RollNO":edit_rollno})
        student.update({"Marks":edit_mark})
        return redirect(url_for('Home'))
    student_edit=student_list[int(index-1)]
    return render_template("edit.html",data=student_edit)

@App.route("/logout")
def logout():
    session.pop("name",None)
    return redirect(url_for("login"))

if __name__ == ("__main__"):
    App.run(debug=True)