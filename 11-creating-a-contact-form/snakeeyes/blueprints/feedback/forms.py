from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms_components import EmailField
from wtforms.validators import DataRequired, Length, Email


class FeedbackForm(FlaskForm):
    email = EmailField(
        "Your email address",
        [DataRequired(), Length(5, 254), Email()])
    message = TextAreaField("Your feedback", [DataRequired(), Length(1, 512)])
