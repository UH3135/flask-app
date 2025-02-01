from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    email = StringField('email', validators=[
        DataRequired(message='이메일을 입력하세요'),
        Email(message='올바른 이메일 형식이 아닙니다')
    ])
    password = PasswordField('password', validators=[
        DataRequired(message='패스워드를 입력하세요'),
        Length(min=8, message='비밀번호는 8자 이상이어야 합니다')
    ])
    submit = SubmitField('로그인')


class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(message='이름을 입력해주세요'), Length(min=2, max=50)])
    password = PasswordField('Password', validators=[
        DataRequired(message='비밀번호를 입력해주세요'), Length(min=8, message='비밀번호는 8자 이상이어야 합니다')
    ])
    email = StringField('Email', validators=[
        DataRequired(message='이메일을 입력해주세요'), Email(message='올바른 이메일 형식이 아닙니다')
    ])
    submit = SubmitField('Sign Up')


