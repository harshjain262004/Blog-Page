from flask import Flask, render_template, request, redirect, session, url_for,flash
from check import *

app=Flask(__name__)
app.secret_key = "BlogPageMinorProject"

@app.route("/")
def index():
    flash("login to view blogs or signup to create account","info")
    return render_template('index.html')

@app.route("/login_page.html", methods=['POST','GET'])
def loginsubmit():
    if request.method=='POST':
        email = request.form['loginpageusername']
        password = request.form['loginpagepassword']
        if check_login(email,password):
            username = get_username(email,password)
            session["user"] = username
            session["email"] = email
            flash("succesful login","info")
            return redirect(url_for("render_blog_page"))
        else:
            res="incorrect credentials or account does not exist"
            return render_template('login_page.html',message = res)
    else:
        res="Please log in to view/add blogs"
        return render_template('login_page.html', message = res)

@app.route("/Blog_page.html", methods=['POST','GET'])
def render_blog_page():
    if "user" in session:
        username = session["user"]
        email = session["email"]
        if request.method=='POST':
            title = request.form['formtitle']
            content = request.form['formcontent']
            add_content(username,title,content)
            content = get_rows_content()
            flash("Post created successfully")
            return redirect(url_for("render_blog_page"))
        else:
            content = get_rows_content()
            return render_template('Blog_page.html',user = username, rows=content)
    else:
        return redirect(url_for("loginsubmit"))


@app.route("/signup_page.html",methods=['POST','GET'])
def signup_page_render():
    if request.method=='POST':
        username = request.form['signuppageusername']
        email = request.form['signuppageemail']
        password = request.form['signuppagepassword']
        if check_signup(email,username,password):
            res = "Account created succesfully"
            flash(res,"info")
            return redirect(url_for("loginsubmit"))
        else:
            res = "Please enter a different Email as this already exists"
            return render_template('signup_page.html',message = res)
    else:
        res=""
        return render_template('signup_page.html',message=res)

@app.route("/logout")
def logout():
    if "user" in session:
        flash("You have been logged out", "info")
    session.pop("user",None)
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run(debug=True)