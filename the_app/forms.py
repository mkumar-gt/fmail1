from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, length

#we need to have some additional validators here later!! Think of allowing
#only email address.

class EmailForm(FlaskForm):
	email_address = StringField('Email Address', validators=[DataRequired()])
	body_text = TextAreaField('Email Body', validators=[DataRequired(), length(max=200)])
	submit = SubmitField('Send Email')