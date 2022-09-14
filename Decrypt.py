class EllipticCurve:
	def __init__(self, a, b, p):
		self.a = a
		self.b = b
		self.p = p 

class Point:
	def __init__(self, x = False, y = False):
		self.x = x
		self.y = y 
		self.o = ((type(x) != int) and (type(y) != int))

	def __eq__(self, q):
		return ((self.x == q.x) and (self.y == q.y)) or self.o == q.o 

	def __ne__(self, q):
		return (self.x != q.x) or (self.y != q.y)

	def __str__(self):
		return f'Point coordinates : ({self.x},{self.y})' if not self.o else f'Point(O)'

	def __add__(self, q, ec = EllipticCurve(497, 1768, 9739)):
		# when p is a point at infinity
		if self.o:
			return q
		# when q is a point at infinity
		if q.o:
			return self
		# when Q = -P
		if self.x == q.x and self.y == -q.y:
			return Point()
		# p and q are different
		if self != q:
			x_inv = pow((q.x - self.x), -1, ec.p)
			l = (q.y - self.y)*x_inv % ec.p
		else:
			y_inv = pow(2*self.y, -1, ec.p)
			l = (3*(self.x**2) + ec.a)*y_inv % ec.p
		res_x = (l**2 - self.x - q.x) % ec.p
		res_y = (l*(self.x - res_x) - self.y) % ec.p
		return Point(res_x, res_y)

num = int(input('How many points would you like to add? : '))
user_input = input('Enter P Coordinates (x,y): ')
x = int(user_input.split(',')[0])
y = int(user_input.split(',')[1])
sum = Point(x, y)

for i in range(1, num):
	str = 'Enter ' + chr(ord('P')+i) + ' Coordinates (x,y): '
	user_input = input(str)
	x = int(user_input.split(',')[0])
	y = int(user_input.split(',')[1])
	sum += Point(x, y)

print(sum)
