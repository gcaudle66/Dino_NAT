from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from webui.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(
                'That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                'That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[
                        FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError(
                    'That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError(
                    'That email is taken. Please choose a different one.')


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')


class ImportCSV(FlaskForm):
    csv = FileField('Import CSV Containing Access Point Descriptors',
                    validators=[FileAllowed(['csv'])])
    description = TextAreaField("Description:", validators=[DataRequired()])
    submit = SubmitField('Import')


class SiteForm(FlaskForm):
    sf_cust_name = StringField(
        'SalesForce Cust Name', validators=[DataRequired()])
    sf_cust_id = StringField('SalesForce Cust ID', validators=[DataRequired()])
    sitename = StringField('New Site Name', validators=[DataRequired()])
    location = StringField('Location-City,ST Zip', validators=[DataRequired()])
    dnac_site = BooleanField('Mirroring a DNAC Site?')
    dnac_site_id = StringField('DNAC Site UUID', validators=[DataRequired()])
    dnac_site_type = StringField(
        'DNAC Site Type-Area,Build,Floor', validators=[DataRequired()])
    dnac_parentId = StringField(
        "DNAC Parent Site's UUID", validators=[DataRequired()])
    dnacSiteNameHierarchy = StringField(
        'DNAC Hierarchy of all Upper UUIDs', validators=[DataRequired()])
    submit = SubmitField("Build It!")


SITE_CHOICES = []
DTYPE_CHOICES = ["9800WLC"]


class DeviceForm(FlaskForm):
    device_name = StringField('Device Name', validators=[DataRequired()])
    device_type = SelectField(label='Device Type', choices=DTYPE_CHOICES)
    device_host_ip = StringField(
        'Hostname/IP', validators=[DataRequired(), Length(min=10, max=50)])
    device_user = StringField('Device Admin Username',
                              validators=[DataRequired()])
    device_pass = PasswordField('Device Password', validators=[DataRequired()])
    content = TextAreaField("Description/Notes (optional):")
    site_id = SelectField(label="Select Site for Device",
                          choices=[SITE_CHOICES])
    submit = SubmitField('Create!')
