from flask import Flask,render_template
from Database import *
app = Flask(__name__, static_path='/static')

@app.route('/')
def hello_world():
   return 'Hello World'


@app.route('/index')
def show_index():
	return render_template("index.html",restaurants=restaurants)

@app.route('/index/<name>')
def show_name(name):
	dict = ['anshal', 'IMRAN', 'sarath']
	print(dict[int(name)])
	return render_template("index.html",name=dict[int(name)])


@app.route('/restaurants')
def show_restaurants():
	return render_template("restaurants.html")

@app.route('/restaurants/<restaurant_id>')
def show_restaurant_menu(restaurant_id):
	print("called restaurant menu")
	return render_template("menu.html",menu=getRestaurantMenu(restaurant_id),restaurant=getRestaurant(restaurant_id))

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

@app.route('/checkout')
def show_checkout():
	return render_template("checkout.html")

@app.route('/order-list')
def show_orderList():
	return render_template("order-list.html")

######### this is a small change made by tdsk

def getRestaurantMenu(restaurant_id):
	for restaurant in restaurantMenu:
		if restaurant['ID'] is int(restaurant_id):
			return restaurant['menu']

def getRestaurant(restaurant_id):
	for restaurant in restaurants:
		if restaurant['ID'] is int(restaurant_id):
			return restaurant

if __name__ == '__main__':
   app.run(debug=True)



