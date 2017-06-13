
class Car(object):

	def __init__(self, car_type="saloon", model="GM", name="General"):

		car_list_exception = ['Porsche', 'Koenigsegg']

		self.car_type = car_type
		self.model = model
		self.name = name
		self.speed = 0
		
		# Except Porsche and Koenigsegg
		if self.name in ['Porsche', 'Koenigsegg']:
			self.number_of_doors = 2
		else:
			self.number_of_doors = 4

		if self.is_saloon() == False:
			self.number_of_wheels = 8
		else:
			self.number_of_wheels = 4

	# Check if car is saloon
	def is_saloon(self):
		if self.car_type == "trailer":
			return False
		else:
			return True

	# Change the speed of the car
	def drive(self, value):
		if self.car_type == "trailer":
			self.speed  = value * 11
		else:
			self.speed = round(value * 333.333)




a = Car("saloon","TG","Porsche")
b = Car("MAN","Truck","trailer")
k= Car('Koenigsegg', 'Agera R')

print(a.number_of_doors)
print(k.number_of_wheels)

