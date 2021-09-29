import random


from restaurant import Restaurant
# 实例不应该与类同名
# restaurant_0 = Restaurant('sunshine','chinese food')
# print(restaurant_0.name)
# print(restaurant_0.type)
# # restaurant_0.number_served = 10
# print(restaurant_0.number_served)
# restaurant_0.describe_restaurant()
# restaurant_0.set_number_served(12)
# restaurant_0.increment_number_served(5)
# restaurant.open_restaurant()

# restaurant_1 = Restaurant('moon','frence')
# restaurant_1.describe_restaurant()
v = random.random()
print(v)
random_1 = []
for i in range(5):
	current_num = random.randint(-100,100)
	# print(current_num)
	random_1.append(current_num)
print(random_1)

class IceCreamStand(Restaurant):
	def __init__(self,restaurant_name,cuisine_type):
		super().__init__(restaurant_name,cuisine_type)
		self.flavors = []

	def show_icecream(self,flavors):
		self.flavors = flavors
		print('we have icecream:')
		for ice in self.flavors:
			print(ice)
# icecream_0 = IceCreamStand('cool','cold')
# flavors = ['sub','yeezy','peat']
# icecream_0.describe_restaurant()
# icecream_0.show_icecream(flavors)