def ifprint(x, y, b, i):
	if b:
		print(f"l{i}: {x=},{y=}")

def Program_1(x,y, print_states = False):
	ifprint(x, y, print_states, 1)
	if x*y > 0:
		ifprint(x, y, print_states, 2)
		x = x-y
		ifprint(x, y, print_states, 3)
		if x**2+y**2 < 100:
			ifprint(x, y, print_states, 4)
			y = -y
			return Program_1(x,y)
		else:
			ifprint(x, y, print_states, "*")
			return x,y
	else:
		ifprint(x, y, print_states, "*")
		return x,y

if __name__ == "__main__":
 	print(Program_1(1,2, True))
