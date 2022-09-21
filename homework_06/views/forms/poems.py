from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class CreatePoemForm(FlaskForm):
    name = StringField(
        label="Poem name",
        name="poem-name",
        validators=[
            DataRequired(),
            Length(min=5),
        ],
    )