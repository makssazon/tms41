from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, PasswordField
from wtforms.validators import Email, DataRequired, Length, EqualTo


class LoginForm(FlaskForm):
    email = StringField('email: ', validators=[Email()])
    psw = PasswordField('psw: ', validators=[DataRequired(), Length(min=4, max=50)])
    remember = BooleanField('remember: ', default=False)
    submit = SubmitField('Enter')


class RegisterForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    email = StringField('email: ', validators=[Email()])
    psw = PasswordField('psw: ', validators=[DataRequired(), Length(min=4, max=50)])
    psw2 = PasswordField('confirm pwd: ',
                         validators=[DataRequired(),
                                     EqualTo('psw', message='pwd and pwd confirm must be the same')])
    submit = SubmitField('register')
