from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Length, EqualTo, Email, data_required, ValidationError
from market.modules import User


class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email(self, email_to_check):
        email = User.query.filter_by(email=email_to_check.data).first()
        if email:
            raise ValidationError('Email Address already exists! Please try a different email address')

    username = StringField(label='Username', validators=[Length(min=2, max=30), data_required()])
    email = StringField(label='Email', validators=[Email(), data_required()])
    password1 = PasswordField(label='Password',validators=[Length(min=6), data_required()])
    password2 = PasswordField(label='Re-type Password', validators=[EqualTo('password1'), data_required()])
    submit = SubmitField(label='Submit')

class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[data_required()])
    password = PasswordField(label='Password:', validators=[data_required()])
    submit = SubmitField(label='Sign in')

class PurchaseForm(FlaskForm):
    submit = SubmitField(label='Purchase Item!')

class SellItemForm(FlaskForm):
    submit = SubmitField(label='Sell Item!')

class ChangePasswordForm(FlaskForm):
    old_password = PasswordField(label='Current Password', validators=[data_required()])
    new_password = PasswordField(label='New Password', validators=[Length(min=6), data_required()])
    confirm_new_password = PasswordField(label='Confirm New Password', validators=[EqualTo('new_password'), data_required()])
    submit = SubmitField(label='Update Password')