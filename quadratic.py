#!/usr/bin/env python3
import math
import cmath
import sys

def get_float(msg, allow_zero):
	x = None
	while x is None:
		try:
			x = float(input(msg))
			if not allow_zero and abs(x) < sys.float_info.epsilon:
				print("Zero is not allow")
				x = None
		except ValueError as e:
			print(e)
	return x

print("ax\N{SUPERSCRIPT TWO} + bx + c = 0")
a = get_float("Enter a:", False)
b = get_float("Enter b:", True)
c = get_float("Enter c:", True)

x1 = None
x2 = None
discriminant = (b ** 2)-(4 * a * c)

if discriminant == 0:
	x1 = -(b / (2*a))
else:
	if discriminant > 0:
		root = math.sqrt(discriminant)
	else:
		root = cmath.sqrt(discriminant)

	x1 = (-b + root) / (2 * a)
	x2 = (-b - root) / (2 * a)

equation = ("{a}x\N{SUPERSCRIPT TWO} + {b}x + {c} = 0 \n"
	"\N{RIGHTWARDS ARROW} x = {x1}").format(**locals())

if x2 is not None:
	equation += (" or x = {}").format(x2)

print(equation)