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

	def __add__(self, q):
		return Addpoint(self, q)


def Addpoint(p, q, ec = EllipticCurve(497, 1768, 9739)):
	# when p is a point at infinity
	if p.o:
		return q
	# when q is a point at infinity
	if q.o:
		return p
	# when Q = -P 
	if p.x == q.x and p.y == -q.y:
		return Point()
	# p and q are different 
	if p != q:
		x_inv = pow((q.x - p.x), -1, ec.p)
		l = (q.y - p.y)*x_inv % ec.p
	else:
		y_inv = pow(2*p.y, -1, ec.p)
		l = (3*(p.x**2) + ec.a)*y_inv % ec.p
	res_x = (l**2 - p.x - q.x) % ec.p
	res_y = (l*(p.x - res_x) - p.y) % ec.p
	return Point(res_x, res_y)

p = Point(493, 5564)
q = Point(1539, 4742)
r = Point(4403, 5202)
 
s = p + p + q + r

print(s)