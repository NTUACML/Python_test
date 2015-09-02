#!/usr/bin/env python3
print("Type integer, each followed by Enter; or ^D or ^Z to finish")

total = 0
count = 0

while True:
	try:
		line = input()
		if line:
			number = int(line)
			total += number
			count += 1
	except ValueError as err:
		print(err)
		continue
	except EOFError:
		break

if count != 0:
	print("Count =", count, "Total =", total, "Mean =", total/count)