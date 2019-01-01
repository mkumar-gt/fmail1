from the_app import app
from flask import render_template
from the_app.forms import EmailForm

@app.route('/send', methods='GET', 'POST')
def send():
	form = EmailForm()
	return render_template('sendmail.html', form=form)