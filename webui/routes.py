from flask import Flask, render_template, url_for, request, redirect, flash
from webui import app
from webui.forms import RegistrationForm, LoginForm
from webui.models import User, Post


@app.route("/home")
@app.route("/")
def home():
	return render_template("home.html", title="Home Page")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/register", methods=["GET", "POST"])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
                flash(f"User Account Created for {form.username.data}!", category="success")
                return redirect(url_for("home"))
	return render_template("register.html", title="Register", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
	form = LoginForm()
	if form.validate_on_submit():
                if form.email.data == "admin@me.com" and form.password.data == "password":
                        flash(f"You have been logged in as {form.email.data}!", "success")
                        return redirect(url_for("home"))
                else:
                        flash("Login unsuccessful. Please check username or password.", "danger")
	return render_template("login.html", title="Login", form=form)

##@app.route("/import", methods=["GET", "POST"])
##def imports():
##	form = PostForm()
##        if user.authenticated:
##        return redirect(request.url)
##        else:
##                flash("Please login first!", "danger")
##                return redirect(url_for("login")
##	return render_template("import.html", title="Import CSV", form=form)
