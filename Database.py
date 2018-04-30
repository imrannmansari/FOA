
class Constants:
	KEY_RESTAURANT_ID = "ID"
	KEY_RESTAURANT_NAME = "NAME"
	KEY_RESTAURANT_LOCATION = "LOCATION"
	KEY_RESTAURANT_DELIVERY_CHARGES = "CHARGES"
	KEY_RESTAURANT_LOGO = "LOGO"
	KEY_MENU_ITEM_ID = "ITEM_ID"
	KEY_MENU_ITEM_COST = "COST"
	KEY_MENU_CUISINE_TYPE = "CUISINE_TYPE"
	KEY_USER_ID = "USID"
	KEY_USER_FNAME = "FN"
	KEY_USER_LNAME = "LN"
	KEY_USER_ADDRESS = "ADDRESS"
	KEY_USER_PHONE = "PHONE"
	KEY_USER_PASS = "PASS"
	KEY_USER_EMAIL = "EMAIL"
	KEY_USER_TYPE = "TYPE"
	


restaurants = [
			{
				Constants.KEY_RESTAURANT_ID : 0,
				Constants.KEY_RESTAURANT_NAME : "PizzaHut",
				Constants.KEY_RESTAURANT_LOCATION : "Patny",
				Constants.KEY_RESTAURANT_DELIVERY_CHARGES : "50",
				Constants.KEY_RESTAURANT_LOGO : "/static/images/restaurent-logo1.jpg"
			},
			{
				Constants.KEY_RESTAURANT_ID : 1,
				Constants.KEY_RESTAURANT_NAME : "Subway",
				Constants.KEY_RESTAURANT_LOCATION : "Patny",
				Constants.KEY_RESTAURANT_DELIVERY_CHARGES : "80",
				Constants.KEY_RESTAURANT_LOGO : "/static/images/restaurent-logo2.jpg"
			},
			{
				Constants.KEY_RESTAURANT_ID : 2,
				Constants.KEY_RESTAURANT_NAME : "Barista",
				Constants.KEY_RESTAURANT_LOCATION : "Patny",
				Constants.KEY_RESTAURANT_DELIVERY_CHARGES : "40",
				Constants.KEY_RESTAURANT_LOGO : "/static/images/restaurent-logo3.jpg"
			},
			{
				Constants.KEY_RESTAURANT_ID : 3,
				Constants.KEY_RESTAURANT_NAME : "Papa John's",
				Constants.KEY_RESTAURANT_LOCATION : "Patny",
				Constants.KEY_RESTAURANT_DELIVERY_CHARGES : "40",
				Constants.KEY_RESTAURANT_LOGO : "/static/images/restaurent-logo4.jpg"
			},
			{
				Constants.KEY_RESTAURANT_ID : 4,
				Constants.KEY_RESTAURANT_NAME : "Dominos",
				Constants.KEY_RESTAURANT_LOCATION : "Patny",
				Constants.KEY_RESTAURANT_DELIVERY_CHARGES : "40",
				Constants.KEY_RESTAURANT_LOGO : "/static/images/restaurent-logo5.jpg"
			},
			{
				Constants.KEY_RESTAURANT_ID : 5,
				Constants.KEY_RESTAURANT_NAME : "KFC",
				Constants.KEY_RESTAURANT_LOCATION : "Patny",
				Constants.KEY_RESTAURANT_DELIVERY_CHARGES : "40",
				Constants.KEY_RESTAURANT_LOGO : "/static/images/restaurent-logo6.jpg"
			},{
				Constants.KEY_RESTAURANT_ID : 6,
				Constants.KEY_RESTAURANT_NAME : "Paradise",
				Constants.KEY_RESTAURANT_LOCATION : "Patny",
				Constants.KEY_RESTAURANT_DELIVERY_CHARGES : "40",
				Constants.KEY_RESTAURANT_LOGO : "/static/images/restaurent-logo7.jpg"
			}
		]

users = [
			{
				Constants.KEY_USER_ID : "anshal_1",
				Constants.KEY_USER_FNAME : "Anshal",
				Constants.KEY_USER_LNAME : "Lad",
				Constants.KEY_USER_ADDRESS : "Andheri",
				Constants.KEY_USER_PHONE : "12323249",
				Constants.KEY_USER_PASS : "awesomelad",
				Constants.KEY_USER_EMAIL : "lad@gmail.com",
				Constants.KEY_USER_TYPE : "admin"
			},
			{
				Constants.KEY_USER_ID : "imran_1",
				Constants.KEY_USER_FNAME : "Imran",
				Constants.KEY_USER_LNAME : "Ansari",
				Constants.KEY_USER_ADDRESS : "Andheri",
				Constants.KEY_USER_PHONE : "78978797",
				Constants.KEY_USER_PASS : "awesomeimran",
				Constants.KEY_USER_EMAIL : "ansari@gmail.com",
				Constants.KEY_USER_TYPE : "customer"
			},
			{
				Constants.KEY_USER_ID : "tdsk_1",
				Constants.KEY_USER_FNAME : "Sarath",
				Constants.KEY_USER_LNAME : "Tdsk",
				Constants.KEY_USER_ADDRESS : "Thumkunta",
				Constants.KEY_USER_PHONE : "6738216",
				Constants.KEY_USER_PASS : "awesometdsk",
				Constants.KEY_USER_EMAIL : "tdsk@gmail.com",
				Constants.KEY_USER_TYPE : "restaurant",
				Constants.KEY_RESTAURANT_ID : 6
			}
		]


restaurantMenu = [
	{
		Constants.KEY_RESTAURANT_ID : 0,
		"menu" : [
			{
				Constants.KEY_MENU_ITEM_ID : "Margretta Pizza",
				Constants.KEY_MENU_ITEM_COST : "220",
				Constants.KEY_MENU_CUISINE_TYPE :"VEG" 
			},{
				Constants.KEY_MENU_ITEM_ID : "Double Paneer Twist Pizza",
				Constants.KEY_MENU_ITEM_COST : "240",
				Constants.KEY_MENU_CUISINE_TYPE :"VEG" 
			},{
				Constants.KEY_MENU_ITEM_ID : "Spicy Chicken Pizza",
				Constants.KEY_MENU_ITEM_COST : "330",
				Constants.KEY_MENU_CUISINE_TYPE :"NON-VEG" 
			}
		]
	},{
		Constants.KEY_RESTAURANT_ID : 1,
		"menu" : [
			{
				Constants.KEY_MENU_ITEM_ID : "Biryani",
				Constants.KEY_MENU_ITEM_COST : "220",
				Constants.KEY_MENU_CUISINE_TYPE :"VEG" 
			},{
				Constants.KEY_MENU_ITEM_ID : "Pizza",
				Constants.KEY_MENU_ITEM_COST : "240",
				Constants.KEY_MENU_CUISINE_TYPE :"VEG" 
			},{
				Constants.KEY_MENU_ITEM_ID : "Noodles",
				Constants.KEY_MENU_ITEM_COST : "130",
				Constants.KEY_MENU_CUISINE_TYPE :"VEG" 
			}
		]
	},{
		Constants.KEY_RESTAURANT_ID : 2,
		"menu" : [
			{
				Constants.KEY_MENU_ITEM_ID : "Biryani",
				Constants.KEY_MENU_ITEM_COST : "220",
				Constants.KEY_MENU_CUISINE_TYPE :"VEG" 
			},{
				Constants.KEY_MENU_ITEM_ID : "Pizza",
				Constants.KEY_MENU_ITEM_COST : "240",
				Constants.KEY_MENU_CUISINE_TYPE :"VEG" 
			},{
				Constants.KEY_MENU_ITEM_ID : "Noodles",
				Constants.KEY_MENU_ITEM_COST : "130",
				Constants.KEY_MENU_CUISINE_TYPE :"VEG" 
			}
		]
	},{
		Constants.KEY_RESTAURANT_ID : 3,
		"menu" : [
			{
				Constants.KEY_MENU_ITEM_ID : "Margretta Pizza",
				Constants.KEY_MENU_ITEM_COST : "220",
				Constants.KEY_MENU_CUISINE_TYPE :"VEG" 
			},{
				Constants.KEY_MENU_ITEM_ID : "Double Paneer Twist Pizza",
				Constants.KEY_MENU_ITEM_COST : "240",
				Constants.KEY_MENU_CUISINE_TYPE :"VEG" 
			},{
				Constants.KEY_MENU_ITEM_ID : "Spicy Chicken Pizza",
				Constants.KEY_MENU_ITEM_COST : "330",
				Constants.KEY_MENU_CUISINE_TYPE :"NON-VEG" 
			}
		]
	},{
		Constants.KEY_RESTAURANT_ID : 4,
		"menu" : [
			{
				Constants.KEY_MENU_ITEM_ID : "Margretta Pizza",
				Constants.KEY_MENU_ITEM_COST : "220",
				Constants.KEY_MENU_CUISINE_TYPE :"VEG" 
			},{
				Constants.KEY_MENU_ITEM_ID : "Double Paneer Twist Pizza",
				Constants.KEY_MENU_ITEM_COST : "240",
				Constants.KEY_MENU_CUISINE_TYPE :"VEG" 
			},{
				Constants.KEY_MENU_ITEM_ID : "Spicy Chicken Pizza",
				Constants.KEY_MENU_ITEM_COST : "330",
				Constants.KEY_MENU_CUISINE_TYPE :"NON-VEG" 
			}
		]
	},{
		Constants.KEY_RESTAURANT_ID : 5,
		"menu" : [
			{
				Constants.KEY_MENU_ITEM_ID : "Biryani",
				Constants.KEY_MENU_ITEM_COST : "220",
				Constants.KEY_MENU_CUISINE_TYPE :"VEG" 
			},{
				Constants.KEY_MENU_ITEM_ID : "Pizza",
				Constants.KEY_MENU_ITEM_COST : "240",
				Constants.KEY_MENU_CUISINE_TYPE :"VEG" 
			},{
				Constants.KEY_MENU_ITEM_ID : "Noodles",
				Constants.KEY_MENU_ITEM_COST : "130",
				Constants.KEY_MENU_CUISINE_TYPE :"VEG" 
			}
		]
	},{
		Constants.KEY_RESTAURANT_ID : 6,
		"menu" : [
			{
				Constants.KEY_MENU_ITEM_ID : "Biryani",
				Constants.KEY_MENU_ITEM_COST : "220",
				Constants.KEY_MENU_CUISINE_TYPE :"VEG" 
			},{
				Constants.KEY_MENU_ITEM_ID : "Pizza",
				Constants.KEY_MENU_ITEM_COST : "240",
				Constants.KEY_MENU_CUISINE_TYPE :"VEG" 
			},{
				Constants.KEY_MENU_ITEM_ID : "Noodles",
				Constants.KEY_MENU_ITEM_COST : "130",
				Constants.KEY_MENU_CUISINE_TYPE :"VEG" 
			}
		]
	}
]


orderQueue = {}

def add_customer(username,password,address,email,phone,fname,lname):
	user = {
		Constants.KEY_USER_ID : username,
		Constants.KEY_USER_FNAME : fname,
		Constants.KEY_USER_LNAME : lname,
		Constants.KEY_USER_ADDRESS : address,
		Constants.KEY_USER_PHONE : phone,
		Constants.KEY_USER_PASS : password,
		Constants.KEY_USER_EMAIL : email,
		Constants.KEY_USER_TYPE : "customer"
	}
	users.append(user);
	
def addRestaurantUser(username,password,address,email,phone,fname,lname):
	user = {
		Constants.KEY_USER_ID : username,
		Constants.KEY_USER_FNAME : fname,
		Constants.KEY_USER_LNAME : lname,
		Constants.KEY_USER_ADDRESS : address,
		Constants.KEY_USER_PHONE : phone,
		Constants.KEY_USER_PASS : password,
		Constants.KEY_USER_EMAIL : email,
		Constants.KEY_USER_TYPE : "restaurant",
		Constants.KEY_RESTAURANT_ID : int(restaurants[-1][Constants.KEY_RESTAURANT_ID])
	}
	print(users)
	users.append(user);
	print(users)

def addRestaurant(name, location, delivery):
	resid = int(restaurants[-1][Constants.KEY_RESTAURANT_ID]) + 1

	restaurant = {
			Constants.KEY_RESTAURANT_ID : resid,
			Constants.KEY_RESTAURANT_NAME : name,
			Constants.KEY_RESTAURANT_LOCATION : location,
			Constants.KEY_RESTAURANT_DELIVERY_CHARGES : delivery
		}

	restaurants.append(restaurant)

def updateRestaurant(restaurant_id,restaurantTable):
	print(int(restaurant_id))
	for restaurant in restaurants:
		print(restaurant['ID'])
		if int(restaurant['ID']) is int(restaurant_id):
			restaurant['NAME'] = restaurantTable[0]['Restaurant Name']
			restaurant['LOCATION'] = restaurantTable[0]['Location']
			restaurant['CHARGES'] = restaurantTable[0]['Delivery Charges']
			restaurant['LOGO'] = restaurantTable[0]['Logo']
	print('updated Restaurant')
	print(restaurants)		

def updateRestaurantMenu(restaurant_id,menuTable):
	for restaurant_menu in restaurantMenu:
		if restaurant_menu['ID'] is int(restaurant_id):
			restaurant_menu['menu'] = menuTable
	print('updated Menu')
	print(restaurantMenu)

def addUserOrder(orderList,username):
	for order in orderList:
		res_id = int(order['restaurant_id'])
		order['user'] = username
		print(order)
		orderQueue.setdefault(res_id, []).append(order)
		print("about to add orde :\n")
		print(order)
	print(orderQueue)	 