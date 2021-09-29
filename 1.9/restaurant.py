class Restaurant:
	def __init__(self,restaurant_name,cuisine_type):
		self.name = restaurant_name
		self.type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print(self.name)
		print(self.type)

	def open_restaurant(self):
		print("Openning...")

	def set_number_served(self,number_served):
		self.number_served = number_served
		print(self.number_served)

	def increment_number_served(self,increment_number):
		self.number_served += increment_number
		print(self.number_served)