
class Constants:
	KEY_RESTAURANT_ID = "ID"
	KEY_RESTAURANT_NAME = "NAME"
	KEY_RESTAURANT_LOCATION = "LOCATION"
	KEY_RESTAURANT_DELIVERY_CHARGES = "CHARGES"


restaurants = [
			{
				Constants.KEY_RESTAURANT_ID : 0,
				Constants.KEY_RESTAURANT_NAME : "Paradise",
				Constants.KEY_RESTAURANT_LOCATION : "Patny",
				Constants.KEY_RESTAURANT_DELIVERY_CHARGES : "40"
			},
			{
				Constants.KEY_RESTAURANT_ID : 1,
				Constants.KEY_RESTAURANT_NAME : "Alpha",
				Constants.KEY_RESTAURANT_LOCATION : "Patny",
				Constants.KEY_RESTAURANT_DELIVERY_CHARGES : "40"
			},
			{
				Constants.KEY_RESTAURANT_ID : 2,
				Constants.KEY_RESTAURANT_NAME : "Elephant",
				Constants.KEY_RESTAURANT_LOCATION : "Patny",
				Constants.KEY_RESTAURANT_DELIVERY_CHARGES : "40"
			},
			{
				Constants.KEY_RESTAURANT_ID : 3,
				Constants.KEY_RESTAURANT_NAME : "Biryani Mahal",
				Constants.KEY_RESTAURANT_LOCATION : "Patny",
				Constants.KEY_RESTAURANT_DELIVERY_CHARGES : "40"
			},
			{
				Constants.KEY_RESTAURANT_ID : 4,
				Constants.KEY_RESTAURANT_NAME : "Pizza Hut",
				Constants.KEY_RESTAURANT_LOCATION : "Patny",
				Constants.KEY_RESTAURANT_DELIVERY_CHARGES : "40"
			}

		]
'''
restaurantMenu = [
	{
		"restaurantID" : 0,
		"menu" : [
			{
				""
			}
		]
	}
]
'''
	
def addRestaurant(name, location, delivery):
	resid = int(restaurants[-1][Constants.KEY_RESTAURANT_ID]) + 1
	restaurant = {
			Constants.KEY_RESTAURANT_ID : resid,
			Constants.KEY_RESTAURANT_NAME : name,
			Constants.KEY_RESTAURANT_LOCATION : location,
			Constants.KEY_RESTAURANT_DELIVERY_CHARGES : delivery
		}

	restaurants.append(restaurant)