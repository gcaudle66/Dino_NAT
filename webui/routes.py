import os
import secrets
import logging
import time
import randfacts
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort, send_from_directory
from flask_table import Table, Col
from webui.data_print import pp_imported_csv, pp_formatted_csv, pp_err_imported_csv
from webui import app, db, bcrypt
from webui.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm, ImportCSV, DeviceForm, SiteForm
from webui.models import User, Post, Import, Device, Site
import mining_csv
from flask_login import login_user, current_user, logout_user, login_required
from logbug import dino_debug

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('dino_debug.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# global parsedCSV_results
parsedCSV_results = []
# global active_dataset_id
# active_dataset_id = int
# global active_dataset_results



@app.route("/")
@app.route("/home")
def home():
    randomf = randfacts.getFact()
    return render_template('home.html', title="Home", randomf=randomf)


@app.route("/devices")
@login_required
def devices():
    if current_user.is_authenticated:
        # page = request.args.get('page', 1, type=int)
        devices = Device.query.order_by(Device.device_name)
        return render_template("devices.html", title="Devices Dashboard", devices=devices)
    else:
        return redirect(url_for("home"))


@app.route("/dashboard")
@login_required
def dashboard():
    if current_user.is_authenticated:
        imports = Import.query.all()
        page = request.args.get('page', 1, type=int)
        posts = Post.query.order_by(
            Post.date_posted.desc()).paginate(page=page, per_page=5)
        return render_template("dashboard1.html", title="User Dashboard", imports=imports)
    else:
        return redirect(url_for("home"))


def set_active_dataset_label(new_label):
    label = new_label
    return label


active_dataset_info = {
    "import_id": "null",
    "import_filename": "null",
    "import_author": "null"
}

# active_dataset_file = "null"
#@set_active_dataset_label(label)


def set_active_dataset_file(import_id):
    active_dataset_file = Import.query.get_or_404(import_id)
    active_dataset_info["import_id"] = import_id
    active_dataset_info["import_filename"] = active_dataset_file.filename
    active_dataset_info["import_author"] = active_dataset_file.author
    return active_dataset_file


@app.route("/dashboard/active-dataset<int:import_id>", methods=["GET"])
@login_required
def active_dataset(import_id):
    if current_user.is_authenticated:
        active_dataset_file = set_active_dataset_file(import_id)
        import_path = os.path.join(
            app.config['UPLOAD_FOLDER'], active_dataset_file.filename)
        parsedCSV_results = mine_csv(import_path)
        # final_CSVresults = format_csv(parsedCSV_results[0])
        print(f"finalCSV index 0 : \n {parsedCSV_results[0]}")
        print(f"finalCSV Err :index 1 : \n {parsedCSV_results[1]}")
        result = pp_formatted_csv(
            parsedCSV_results[0], f'active_dataset{import_id}')
        err_result = pp_err_imported_csv(
            parsedCSV_results[1], f'active_dataset{import_id}')
        print(err_result)
        active_dataset_id = str('import_id')
        # active_dataset_results = result
        return render_template('active.html', title='Active DataSet File', results=result, active=active_dataset_info, err_results=err_result)
    else:
        flash("You must be logged in to access this page", "danger")
        return redirect(url_for("Home"))


@login_required
@app.route("/flows/ap-renamerer", methods=['GET'])
def flow_ap_renamerer():
    if current_user.is_authenticated:
        return render_template("flow_ap_renamerer.html", title="Dino Flow-AP Renamerer")
    else:
        flash("You must be logged in to access this page", "danger")
        return redirect(url_for("home"))


@login_required
@app.route("/flows/flow-ap-tagging", methods=['GET'])
def flow_ap_tagging():
    if current_user.is_authenticated:
        return render_template("flow_ap_tagging.html", title="Dino Flow-AP Tagging Maintenance")
    else:
        flash("You must be logged in to access this page", "danger")
        return redirect(url_for("home"))

@app.route("/flows", methods=['GET'])
def flows():
    if current_user.is_authenticated:
        return render_template("flows.html", title="IBN Flows for You!", active=active_dataset_info)
    else:
        flash("You must be logged in to access this page", "danger")
        return redirect(url_for("home"))


@app.route("/about", methods=['GET'])
def about():
    return render_template("about.html", title="About")


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(username=form.username.data,
                    email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/device/new", methods=['GET', 'POST'])
def create_device():
    if current_user.is_authenticated:
        form = DeviceForm()
        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(
                form.device_password.data).decode('utf-8')
            device = Device(device_name=form.device_name.data, device_type=form.device_type.data, device_host_ip=form.device_host_ip.data, device_user=form.device_user.data,
                            device_pass=hashed_password, content=form.content.data, site_id=form.site_id.data, date_posted=form.date_posted.data, user_id=current_user.user_id)
            db.session.add(device)
            db.session.commit()
            flash('Your device has been created! You are now able view it', 'success')
            return redirect(url_for('devices'))
    return render_template('create_device.html', title='New Device', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('dashboard'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(
        app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for(
        'static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account',
                           image_file=image_file, form=form)


def mine_csv(csv_file):
    parsedCSV_results = []
    parsedCSV_results = mining_csv.parseCSV(csv_file)
    return parsedCSV_results


# def format_csv(parsedCSV_results):
#     final_CSVresults = mining_csv.formatMacs(parsedCSV_results)
#     return final_CSVresults


def save_csv(import_csv):
    random_hex = secrets.token_hex(8)
    f_name, f_ext = os.path.splitext(import_csv.filename)
    csv_fn = f_name + random_hex + f_ext
    save = import_csv.save(os.path.join(app.config['UPLOAD_FOLDER'], csv_fn))
    return csv_fn


@app.route('/index', methods=["GET", "POST"])
@login_required
def index():
    if current_user.is_authenticated:
        files = os.listdir(app.config['UPLOAD_FOLDER'])
        return render_template('index.html', files=files)
    else:
        flash("You are not authorized to access this page!", "danger")
        return redirect(url_for("login"))


@app.route("/uploads/<filename>")
def upload(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route("/importcsv", methods=["GET", "POST"])
@login_required
def import_csv():
    form = ImportCSV()
    import_csv = request.files.getlist('file')
#    if import_csv.filename != "":
    if form.validate_on_submit():
        if form.csv.data:
            csv_fn = save_csv(form.csv.data)
            insert = Import(
                filename=csv_fn, description=form.description.data, author=current_user)
            db.session.add(insert)
            db.session.commit()
            flash(f'Your file {csv_fn} has been imported!', 'success')
            csv_fn = current_user.imports
            return redirect(url_for('dashboard'))
    elif request.method == "GET":
        redirect(url_for('dashboard'))
        current_user.imports = current_user.imports
        current_user.username = current_user.username
    return render_template('import_csv.html', title='New Import',
                           form=form, legend=form.csv.label)


@app.route("/imports/<int:import_id>")
@login_required
def imports(import_id):
    imported = Import.query.get_or_404(import_id)
    post = imported
    datafile = os.path.join(app.config['UPLOAD_FOLDER'], imported.filename)
    csv_data = pp_imported_csv(datafile)
    return render_template('imports.html', title='Imported File Mgmnt', imported=imported, df=csv_data)


@app.route("/imports/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_import(post_id):
    post = Import.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your import has been deleted!', 'success')
    return redirect(url_for('dashboard'))


@app.route("/imports/<int:import_id>/update", methods=['GET', 'POST'])
@login_required
def update_imported(import_id):
    imported = Import.query.get_or_404(import_id)
    if imported.author != current_user:
        abort(403)
    form = ImportCSV()
    if form.validate_on_submit():
        imported.filename = form.csv.data
        imported.description = form.description.data
        db.session.commit()
        flash('Your import has been updated!', 'success')
        return redirect(url_for('dashboard', import_id=imported.id))
    elif request.method == 'GET':
        form.csv.data = imported.filename
        form.description.data = imported.description
    return render_template('import_csv.html', title='Update Import', form=form)


@app.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data,
                    content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('create_post.html', title='New Post',
                           form=form, legend='New Post')


@app.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@app.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post',
                           form=form, legend='Update Post')


@app.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('home'))
