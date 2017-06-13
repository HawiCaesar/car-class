
class Car(object):

	def __init__(self, name="General" ,model="GM", car_type=""):

		self.car_type = car_type
		self.model = model
		self.name = name
		self.speed = 0
		
		
		# Except Porsche and Koenigsegg
		if self.name in ['Porsche', 'Koenigsegg']:
			self.number_of_doors = 2
		else:
			self.number_of_doors = 4


		#check if car type is trailer
		if self.car_type == "trailer":
			self.number_of_wheels = 8
		else:
			self.number_of_wheels = 4


	#Check if car is saloon based on wheels
	def is_saloon(self):
		if self.number_of_wheels == 8:
			return False
		else:
			return True

	# Change the speed of the car
	def drive(self, value):
		if self.car_type == "trailer":
			self.speed  = value * 11
		else:
			self.speed = round(value * 333.333)




b = Car("MAN","Truck","trailer")
k= Car('Koenigsegg', 'Agera R')

print(k.number_of_wheels)
print(b.number_of_wheels)
print(b.is_saloon())

