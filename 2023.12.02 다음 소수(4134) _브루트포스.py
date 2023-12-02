import sys
input = sys.stdin.readline



def getPrime(x):
	if x == 0 or x == 1:
		return False
	for i in range(2,int(x**0.5)+1):
		if x % i == 0:
			return 0
	return 1


t = int(input())
for i in range(t):
	n = int(input())
	while True:
		if getPrime(n):
			print(n)
			break
		else:
			n+=1



# p = [[getPrime(i),i] for i in range(4*(10**9)+1)]

# p = [[getPrime(i),i] for i in range(4*(10**9)+1)]
# # p.sort(key=lambda x: (-x[0],x[1]))


# print()
# # t = int(input())

# # for i in range(t):
# # 	n = int(input())
# # 	print(n)
# # 	print(sorted(p[n+1:],key=lambda x: (-x[0],x[1]))[0][1])
# # 	print(sorted(p[n+1:],key=lambda x: (-x[0],x[1])))
# # # 	print(p[n+1:][0])
# # 	# while True:
# # 	# 	n+=1
# # 	# 	if getPrime(n):
# # 	# 		print(n)
# # 	# 		break

