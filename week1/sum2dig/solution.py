import fileinput

input = next(fileinput.input())
tokens = input.split()
print(int(tokens[0]) + int(tokens[1]))
