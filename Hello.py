from flask import Flask,render_template
app = Flask(__name__, static_path='/static')

@app.route('/')
def hello_world():
   return 'Hello World'


@app.route('/index')
def show_index():
	return render_template("index.html")

@app.route('/index/<name>')
def show_name(name):
	dict = ['anshal', 'IMRAN']
	print(dict[int(name)])
	return render_template("index.html",name=dict[int(name)])


@app.route('/restaurants')
def show_restaurants():
	return render_template("restaurants.html")


@app.route('/order')
def show_order():
	return render_template("order.html")


@app.route('/contact')
def show_contact():
	return render_template("contact.html")


@app.route('/login')
def show_login():
	return render_template("login.html")


@app.route('/register')
def show_admin():
	return render_template("register.html")

######### this is a small change made by tdsk

if __name__ == '__main__':
   app.run(debug=True)
