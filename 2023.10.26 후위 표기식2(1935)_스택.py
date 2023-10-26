import sys
input = sys.stdin.readline

n = int(input())
s = list(input().rstrip())
arr = [int(input()) for _ in range(n)]
tmp = 0
answer = []
for i in s:
	if i.isalnum():
		answer.append(arr[ord(i)-65])
	else:
		a = answer.pop()
		b = answer.pop()
		if i =='+':
			tmp = a+b
		elif i == '*':
			tmp = a*b
		elif i == '/':
			tmp = float(b/a)
		else:
			tmp = b-a
		answer.append(tmp)

print('%.2f'%answer[-1])

# print(`%.2f` tmp)





# print(ord('A'))
# print(ord('B'))
# print(ord('C'))

