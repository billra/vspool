# V plotter with spool kinematics
# Bill Ola Rasmussen
# version 0.1
from math import sqrt, acos, atan2, sin, cos, pi

def vspoolinverse(Cx,Cy,Px,Py,r):
	# right triangle calculation to find tangent point
	h = sqrt((Px - Cx) ** 2 + (Py - Cy) ** 2)
	b = acos(r / h)
	m = atan2(Py - Cy,Px - Cx)
	Tx = Cx + r * cos(m + b)
	Ty = Cy + r * sin(m + b)
	# find length of arc
	n = atan2(Ty - Cy, Tx - Cx)
	a = pi / 2 - n
	c = a * r
	# find length of straight line
	s = sqrt((Px - Tx) ** 2 + (Py - Ty) ** 2)
	# return total length
	cs = c + s
	return cs

def vspoolinversecc(Cx,Cy,Px,Py,r): # counter clockwise
	# right triangle calculation to find tangent point
	h = sqrt((Px - Cx) ** 2 + (Py - Cy) ** 2)
	b = acos(r / h)
	m = atan2(Py - Cy,Px - Cx)
	Tx = Cx + r * cos(m - b) # note
	Ty = Cy + r * sin(m - b) # note
	# find length of arc
	n = atan2(Ty - Cy, Tx - Cx)
	a = pi*1.5 + n # note
	c = a * r
	# find length of straight line
	s = sqrt((Px - Tx) ** 2 + (Py - Ty) ** 2)
	cs = c + s
	return cs

def main():
	print('V Spool Kinematics')

	Cx,Cy = 0,4 # center of spool
	Px,Py = 7,-1 # point being plotted
	r = 3 # radius of spool

	cs = vspoolinverse(Cx,Cy,Px,Py,r)
	print('control line length:', cs)

	Py = 0
	cs = vspoolinverse(Cx,Cy,Px,Py,r)
	print('control line length:', cs)

	print('done.')

if __name__ == "__main__":
	main()
