# Incremental Version 4
# - add is_orthogonal_to judgment
# - add is_parallel_to judgment
# - add is_zero judgmeent

from math import sqrt, acos, pi
from decimal import Decimal, getcontext #better numerical precision

getcontext().prec = 30

class Vector(object):

	CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'

	def __init__(self, coordinates):
		try:
			if not coordinates:
				raise ValueError
			#ensure floating numbers
			self.coordinates = tuple([Decimal(x) for x in coordinates])
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
			return self.times_scalar(Decimal('1.0')/magnitude)

		except ZeroDivisionError:
			raise Exception('Cannot normalize the zero vector')

	def is_orthogonal_to(self, v, tolerance = 1e-10):
		return abs(self.dot(v)) < tolerance

	def is_parallel_to(self,v):
		return ( self.is_zero() or 
						 v.is_zero() or
						 self.angle_with(v) == 0 or
						 self.angle_with(v) == pi)

	def is_zero(self, tolerance = 1e-10):
		return self.magnitude() < tolerance

	def dot(self,v):
		return sum(x * y for x, y in zip(self.coordinates, v.coordinates))

	def angle_with(self, v, in_degrees=False):
		try:
			u1 = self.normalized()
			u2 = v.normalized()
			angle_in_radians = acos(u1.dot(u2))

			if in_degrees:
				degrees_per_radian = 180. / pi
				return angle_in_radians * degrees_per_radian
			else:
				return angle_in_radians

		except Exception as e:
			if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
				raise Exception("Cannot compute an angle with zero vector")
			else:
				raise e

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

