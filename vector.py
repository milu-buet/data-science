import math

class Vector:
	def __init__(self, a, b):
		self.x = a
		self.y = b

	def __mul__(self, u):
		if type(u) in [int, float]:
			return Vector(u*self.x, u*self.y)
		return self.x * u.x + self.y * u.y

	def __len__(self):
		return int(math.sqrt(self.x**2 + self.y**2))

	def __eq__(self, x):
		return [x]*10

	def __contains__(self, a):
		return self.x==a or self.y==a

	def print(self):
		print(self, self.x, self.y)
#---------------------------------------

v = Vector(3,4)
u = Vector(7,12)

print( v * u )
print( len(v) )
print( v == 5 )
print( 5 in v )
w = v * 10
w.print()
