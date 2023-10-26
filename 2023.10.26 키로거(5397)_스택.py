import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
	l_L = []
	r_L = []
	word = input().rstrip()

	for i in word:
		if i == '-':
			if l_L:
				l_L.pop()
		elif i == '<':
			if l_L:
				r_L.append(l_L.pop())
		elif i == '>':
			if r_L:
				l_L.append(r_L.pop())
		else:
			l_L.append(i)
	l_L.extend(reversed(r_L))
	print(''.join(l_L))
