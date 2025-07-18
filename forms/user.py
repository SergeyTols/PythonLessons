from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields.simple import EmailField, TextAreaField
from wtforms.validators import DataRequired

class Register(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired('Введите корректный Email')])
    password = PasswordField('Пароль', validators=[DataRequired('Введите пароль')])
    password_again = PasswordField('Подтвердите пароль', validators=[DataRequired('Подтвердите пароль')])
    name = StringField('Ваше имя', validators=[DataRequired('Введите ваше имя')])
    about = TextAreaField('Немного о себе')
    submit = SubmitField('Регистрация')