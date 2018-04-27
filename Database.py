
class Constants:
	KEY_RESTAURANT_ID = "ID"
	KEY_RESTAURANT_NAME = "NAME"
	KEY_RESTAURANT_LOCATION = "LOCATION"
	KEY_RESTAURANT_DELIVERY_CHARGES = "CHARGES"
	KEY_RESTAURANT_LOGO = "LOGO"
	KEY_MENU_ITEM_ID = "ITEM_ID"
	KEY_MENU_ITEM_COST = "COST"
	KEY_MENU_CUISINE_TYPE = "CUISINE_TYPE"

restaurants = [
			{
				Constants.KEY_RESTAURANT_ID : 0,
				Constants.KEY_RESTAURANT_NAME : "PizzaHut",
				Constants.KEY_RESTAURANT_LOCATION : "Patny",
				Constants.KEY_RESTAURANT_DELIVERY_CHARGES : "40",
				Constants.KEY_RESTAURANT_LOGO : "/static/images/restaurent-logo1.jpg"
			},
			{
				Constants.KEY_RESTAURANT_ID : 1,
				Constants.KEY_RESTAURANT_NAME : "Subway",
				Constants.KEY_RESTAURANT_LOCATION : "Patny",
				Constants.KEY_RESTAURANT_DELIVERY_CHARGES : "40",
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

	
def addRestaurant(name, location, delivery):
	resid = int(restaurants[-1][Constants.KEY_RESTAURANT_ID]) + 1
	restaurant = {
			Constants.KEY_RESTAURANT_ID : resid,
			Constants.KEY_RESTAURANT_NAME : name,
			Constants.KEY_RESTAURANT_LOCATION : location,
			Constants.KEY_RESTAURANT_DELIVERY_CHARGES : delivery
		}

	restaurants.append(restaurant)