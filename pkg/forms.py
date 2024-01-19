from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField, BooleanField, DateField, TextAreaField, FileField
from wtforms.validators import DataRequired, Email, URL, Length
from flask_wtf.file import FileField, FileAllowed, FileRequired

class BreakoutForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    # level = StringField('Level', validators=[DataRequired()])
    image = FileField('Upload Cover', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png'],"we only allow images")])
    # status = RadioField('Status', validators=[DataRequired()])
    submit = SubmitField('Add Topic!')