# V plotter with spool kinematics
# Bill Ola Rasmussen
# version 0.1
from math import sqrt, acos, atan2, sin, cos, pi

def vspoolinverse(Cx,Cy,Px,Py,r):
	h = sqrt((Px - Cx) ** 2 + (Py - Cy) ** 2)
	b = acos(r / h)
	m = atan2(Py - Cy,Px - Cx)
	Tx = Cx + r * cos(m + b)
	Ty = Cy + r * sin(m + b)
	n = atan2(Ty - Cy, Tx - Cx)
	a = pi / 2 - n
	c = a * r
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
