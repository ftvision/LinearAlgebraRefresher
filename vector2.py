# Incremental Version 2
# - add plus, minus, scaling, magnitude, normalization

from math import sqrt, acos, pi

class Vector(object):

	def __init__(self, coordinates):
		try:
			if not coordinates:
				raise ValueError
			self.coordinates = tuple(coordinates)
			self.dimension 	 = len(coordinates) 

		except ValueError:
			raise ValueError('The coordinate must be nonempty')

		except TypeError:
			raise TypeError('The coordinates must be an iterable')

	def plus(self, v):
		new_coordinates = [x + y for x, y in zip(self.coordinates, v.coordinates)]
		return Vector(new_coordinates)

	def minus(self, v):
		new_coordinates = [x - y for x, y in zip(self.coordinates, v.coordinates)]
		return Vector(new_coordinates)

	def times_scalar(self, c):
		new_coordinates = [c * x for x in self.coordinates]
		return Vector(new_coordinates)

	def magnitude(self):
		return sqrt(sum(x ** 2 for x in self.coordinates))

	def normalized(self):
		try:
			magnitude = self.magnitude()
			return self.times_scalar(1./magnitude)

		except ZeroDivisionError:
			raise Exception('Cannot normalize the zero vector')

	def __str__(self):
		return 'Vector: {}'.format(self.coordinates)

	def __eq__(self, v):
		return self.coordinates == v.coordinates

#initiate a new Vector
my_vector = Vector([1,2,3])
print my_vector
my_vector2 = Vector([1,2,3])
my_vector3 = Vector([4,5,6])
print my_vector == my_vector2
print my_vector == my_vector3
#comment on string.format()
#Format strings contain “replacement fields” surrounded by curly braces {}.
#Anything that is not contained in braces is considered literal text, 
#which is copied unchanged to the output. 

#If you need to include a brace character in the literal text, 
#it can be escaped by doubling: {{ and }}.

