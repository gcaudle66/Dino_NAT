from flask import Flask, render_template, url_for, request, redirect, flash
from webui import app, db, bcrypt
from webui.forms import RegistrationForm, LoginForm
from webui.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/home")
@app.route("/")
def home():
	return render_template("home.html", title="Home Page")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/register", methods=["GET", "POST"])
def register():
        if current_user.is_authenticated:
                return redirect(url_for('home'))
        form = RegistrationForm()
        if form.validate_on_submit():
                hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
                user = User(username=form.username.data, email=form.email.data, password=hashed_password)
                db.session.add(user)
                db.session.commit()
                flash('Your account has been created! You are now able to log in', 'success')
                return redirect(url_for('login'))
        return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)#, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)
##@app.route("/import", methods=["GET", "POST"])
##def imports():
##	form = PostForm()
##        if user.authenticated:
##        return redirect(request.url)
##        else:
##                flash("Please login first!", "danger")
##                return redirect(url_for("login")
##	return render_template("import.html", title="Import CSV", form=form)

@app.route("/review")
def review():
        file = "example_import_ap_map_ALL.csv"
        parsedCSVresults = mine_wlc_ap.parseCSV(file)
        return render_template("review.html", post=parsedCSV_results)

@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('home'))
