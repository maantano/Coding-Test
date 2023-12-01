# import sys
# input = sys.stdin.readline
# r,b = map(int,input().split())

# total = r+b

# def division(x):
# 	answer  = []
# 	for i in range(1,int(x**0.5)+1):
# 		if x % i == 0:
# 			answer.append(i)
# 			if i ** 2 != x:
# 				answer.append(x//i)
# 	return sorted(answer)

# answer = division(total)

# if len(answer) == 3:
# 	print(answer[1],answer[1],sep=' ')
# else:
# 	print(answer[len(answer)//2],answer[len(answer)//2 - 1],sep=' ')



r, b = map(int, input().split())

l, w = 0, 0
for i in range(3,3000):
	for j in range(3,3000):
		if i*2 + (j-2)*2 == r and (i-2)*(j-2) == b:
			l , w = i, j
			break
	if l != 0:
		break

if w > l:
	l, w = w, l

print(l, w)
