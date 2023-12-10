n,m = map(int,input().split(' '))
# 24 18

# 6
# 72
# import math

# a, b = map(int, input().split())

# print(math.gcd(a, b))
# print(math.lcm(a, b))



a, b = map(int, input().split())

def gcd(a, b):
	while b > 0:
		a, b = b, a % b
	return a

def lcm(a, b):
	return a * b // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b))
