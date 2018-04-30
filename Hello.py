from flask import Flask,render_template,request,make_response,redirect,url_for
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
	return render_template("restaurants.html",restaurants=restaurants)

@app.route('/restaurants/<restaurant_id>')
def show_restaurant_menu(restaurant_id):
	print("called restaurant menu")
	return render_template("menu.html",menu=getRestaurantMenu(restaurant_id),restaurant=getRestaurant(restaurant_id),restaurants=restaurants)

@app.route('/order')
def show_order():
	return render_template("order.html")


@app.route('/contact')
def show_contact():
	return render_template("contact.html")

@app.route('/login')
def show_login():
	return render_template("login.html")

def open_admin():
	return render_template("admin.html")

def manage_restaurant(restaurant_id):
	if int(restaurant_id) not in orderQueue:
		orderQueue[int(restaurant_id)] = []
		myOrder = []
	else:
		myOrder = orderQueue[int(restaurant_id)]
	print(myOrder)
	return render_template("manage_restaurant.html",menu=getRestaurantMenu(str(restaurant_id)),restaurant=getRestaurant(str(restaurant_id)),restaurants=restaurants,myOrder=myOrder)

@app.route('/authenticate_login', methods = ['POST', 'GET'])
def set_cookie():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']

	print(username)
	print(password)

	type = validUser(username,password)
	if type:
		if type == "restaurant":
			print('calling resid with username : ' + username)
			restaurant_id1=getRestaurantId(username)
			resp = make_response(manage_restaurant(restaurant_id=restaurant_id1))
			if request.cookies.get('username') != None:
				resp.set_cookie('orderList','')
				resp.set_cookie('totalAmnt','')
			resp.set_cookie('username', username)
			resp.set_cookie('correctLogin', "true")
		elif type == "admin":
			print(username)
			resp = make_response(open_admin())
			if request.cookies.get('username') != None:
				resp.set_cookie('orderList','')
				resp.set_cookie('totalAmnt','')
			resp.set_cookie('username', username)
			resp.set_cookie('correctLogin', "true")
		else:
			print(username)
			resp = make_response(redirect(url_for('show_index')))
			print(request.cookies.get('username'))
			if request.cookies.get('username') != None:
				resp.set_cookie('orderList','')
				resp.set_cookie('totalAmnt','')
			resp.set_cookie('username', username)
			resp.set_cookie('correctLogin', "true")
		
	else :
		resp = make_response(redirect(url_for('show_login')))
		resp.set_cookie('correctLogin', "false")
	return resp

@app.route('/register')
def show_admin():
	return render_template("register.html")

@app.route('/register_customer', methods = ['POST', 'GET'])
def register_customer():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		address = request.form['address']
		email = request.form['email']
		phone = request.form['phone']
		fname = request.form['fname']
		lname = request.form['lname']

	add_customer(username,password,address,email,phone,fname,lname)	
	return redirect(url_for('show_login'))

@app.route('/register_restaurant', methods = ['POST', 'GET'])
def register_restaurant():
	if request.method == 'POST':
		res_name = request.form['name']
		location = request.form['location']
		charges = request.form['charges']
		username = request.form['username']
		password = request.form['password']
		address = request.form['address']
		email = request.form['email']
		phone = request.form['phone']
		fname = request.form['fname']
		lname = request.form['lname']
		
	addRestaurant(res_name,location,charges)
	addRestaurantUser(username,password,address,email,phone,fname,lname)	
	return redirect(url_for('show_login'))


@app.route('/checkout')
def show_checkout():
	return render_template("checkout.html",restaurants=restaurants)

@app.route('/order-list')
def show_orderList():
	return render_template("order-list.html")

@app.route('/place_order', methods=['POST'])
def place_order():
	print("hello i am here")
	orderList = request.get_json(force=True)
	username = request.cookies.get('username')
	addUserOrder(orderList,username)

	# orderList = request.form.getList("orderList[]")
 	# orderList = request.get_json()
 	# orderList = request.get_json()
	return render_template("index.html")

@app.route('/update_restaurant', methods=['POST'])
def update_restaurant():
	print("hey updateing res")
	data = request.get_json(force=True)
	print(data)
	restaurant_id = data['res_id']
	menuTable = data['menuTable']
	restaurantTable = data['restaurantTable']
	print(restaurant_id)
	print(menuTable)
	print(restaurantTable)
	
	f= open('log.txt',"a+")

	updateRestaurant(restaurant_id,restaurantTable)
	f.write("updateing rest")
	updateRestaurantMenu(restaurant_id,menuTable)
	f.write("updateing restMenu")
	f.close()
	return render_template("index.html")


 	
######### this is a small change made by tdsk

def getRestaurantMenu(restaurant_id):
	for restaurant in restaurantMenu:
		if restaurant['ID'] is int(restaurant_id):
			return restaurant['menu']

def getRestaurant(restaurant_id):
	for restaurant in restaurants:
		if restaurant['ID'] is int(restaurant_id):
			return restaurant

def getRestaurantId(username):
	print('gettin res id for ' + username)
	for user in users:
		if user['USID'] == username:
			print(user['USID'] + "has matched")
			print(user['ID'])
			return user['ID']

def validUser(username,password):
	print(username + " " +password)
	for x in users :
		print(x['PASS'] + " " + password)
		if (x['USID'] == username) and (x['PASS'] == password) :
			return x['TYPE']
	return False

if __name__ == '__main__':
   app.run(debug=True)



