# Incremental Version 6
# - add cross product
# - add area of the parallelogram spanned by v, w
# - add area of the triangle spanned by v, w


from math import sqrt, acos, pi
from decimal import Decimal, getcontext #better numerical precision

getcontext().prec = 30

class Vector(object):

	CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'
	NO_UNIQUE_PARALLEL_COMPONENT_MSG = 'No unique parallel component'
	NO_UNIQUE_ORTHOGONAL_COMPONENT_MSG = 'No unique orthogonal component'
	ONLY_DEFINED_IN_TWO_THREE_DIMS_MSG = 'Onyl defined in two 3D vectors'
	
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

	def component_orthogonal_to(self, basis):
		try:
			projection = self.component_parallel_to(basis)
			return self.minus(projection)

		except Exception as e:
			if str(e) == self.NO_UNIQUE_PARALLEL_COMPONENT_MSG:
				raise Exception(self.NO_UNIQUE_ORTHOGONAL_COMPONENT_MSG)
			else:
				raise e

	def component_parallel_to(self, basis):
		try:
			u = basis.normalized()
			weight = self.dot(u)
			return u.times_scalar(weight)

		except Exception as e:
			if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
				raise Exception(self.NO_UNIQUE_PARALLEL_COMPONENT_MSG)
			else:
				raise e

	def dot(self,v):
		return sum(x * y for x, y in zip(self.coordinates, v.coordinates))

	def area_of_triangle_with(self, v):
		return self.area_of_parallelogram_with(v) / Decimal('2.0')

	def area_of_parallelogram_with(self, v):
		cross_product = self.cross(v)
		return cross_product.magnitude()

	def cross(self, v):
		try:
			x_1, y_1, z_1 = self.coordinates
			x_2, y_2, z_2 = v.coordinates
			new_coordinates = [ y_1 * z_2 - y_2 * z_1, 
												 -(x_1 * z_2 - x_2 * z_1),
												  x_1 * y_2 - x_2 * y_1]
			return Vector(new_coordinates)

		except ValueError as e:
			msg = str(e)
			if msg == 'need more than 2 values to unpack':
				"""if vectors are in two dimension, add 0 to the 3rd dimention"""
				self_embedded_in_R3 = Vector(self.coordinates + ('0', ))
				v_embedded_in_R3 = Vector(v.coordinates + ('0', ))
				return self_embedded_in_R3.cross(v_embedded_in_R3)
			elif (msg == 'too many value to unpack' or msg == 'need more than 1 value to unpack'):
				raise Exception(self.ONLY_DEFINED_IN_TWO_THREE_DIMS_MSG)
			else:
				raise e

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
v = Vector([1,2,3])
w = Vector([2,3,4])
v.method()
v.method(w)
