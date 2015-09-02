#!/usr/bin/env python3
Num = -205

if Num >= 100:
	print("Large than 100")
elif Num < 100:
	print("Small than 100")
else:
	print("I don't know")

Item = ["Go", 1, "Kavy", Num]
Item += ["I love","NaNa"] #append

for i in Item:
	print(i)

