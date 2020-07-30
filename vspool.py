# V plotter with spool kinematics
# Bill Ola Rasmussen
# version 0.1
from math import sqrt, acos, atan2, sin, cos, pi

# inverse calculation: from plot points x,y find control line length
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
	# instead of counter clockwise calculation,
    # simply vertical mirror plot point from center of circle
    # to get the counter clockwise length
	return vspoolinverse(Cx,Cy,2 * Cx - Px,Py,r)

# forward calculation: from control line length and angle find plot point
# note: intermediate calculation, actual forward calculation is from two
# control line lengths

def vspoolforward(cx,cy,r,cs,n):
	# find tangent point
	tx = cx + r * cos(n)
	ty = cy + r * sin(n)
	# find plot point
	a = pi / 2 - n
	c = a * r
	s = cs - c
	x = tx + s * cos(-a)
	y = ty + s * sin(-a)
	return x,y

def vspoolforward_alt(cx,cy,r,cs,n): # another method to do same calcluation
	a = pi / 2 - n
	c = a * r
	s = cs - c
	b = atan2(s,r)
	m = n - b
	h = sqrt(r ** 2 + s ** 2)
	x = cx + h * cos(m)
	y = cy + h * sin(m)
	return x,y

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
