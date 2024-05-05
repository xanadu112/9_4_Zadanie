from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, BooleanField
from wtforms.validators import DataRequired

class BookForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    author = StringField("Author", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    num_pages = IntegerField("Number of pages", validators=[DataRequired()])
    read = BooleanField("Has it been read?")
    
    submit = SubmitField("Add Book")
