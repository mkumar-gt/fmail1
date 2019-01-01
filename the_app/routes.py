from the_app import app

@app.route('/')
@app.route('/send')
def send():
	return "app being built"