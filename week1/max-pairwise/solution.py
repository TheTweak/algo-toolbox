import fileinput

input = fileinput.input()
n = next(input)
arr = [int(x) for x in next(input).split()]

arr_max = 0
arr_2nd_max = 0
for x in arr:
	if x > arr_max:
		arr_2nd_max = arr_max
		arr_max = x
	elif x > arr_2nd_max:
		arr_2nd_max = x

print(arr_2nd_max * arr_max)