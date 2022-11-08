def Program_1(x,y):
	if x*y > 0:
		return x,y
	else:
		x = x-y
		if x**2+y**2 < 100:
			y = -y
			return Program_1(x,y)
		else:
			return x,y