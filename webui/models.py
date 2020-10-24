from datetime import datetime
from webui import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False,
                           default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    imports = db.relationship('Import', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}', '{self.imports}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


class Import(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    filename = db.Column(db.String(64), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)

    def __repr__(self):
        return f"Import('{self.id}', '{self.filename}', '{self.user_id}', '{self.description}')"


class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device_name = db.Column(db.String(100), nullable=False)
    device_type = db.Column(db.String(100), nullable=False)
    device_host_ip = db.Column(db.String(50), nullable=False)
    device_user = db.Column(db.String(20), nullable=True)
    device_pass = db.Column(db.String(60), nullable=True)
    content = db.Column(db.Text, nullable=True)
    site_id = db.Column(db.Integer, db.ForeignKey('site.id'), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Device('{self.device_name}', '{self.site_id}', '{self.device_type}', '{self.user_id}', '{self.date_posted}')"


class Site(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sitename = db.Column(db.String(30), unique=True, nullable=False)
    location = db.Column(db.String(120), nullable=True)
    dnac_site = db.Column(db.Boolean(), nullable=True)
    device_user = db.Column(
        db.String(20), nullable=False, default='default.jpg')
    device_pass = db.Column(db.String(60), nullable=False)
    devices = db.relationship('Device', backref='device', lazy=True)
    created_by = db.Column(
        db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        # , '{self.email}', '{self.image_file}', '{self.imports}')"
        return Site(f"{self.sitename}")
