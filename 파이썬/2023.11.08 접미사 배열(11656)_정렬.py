n = input()
answer = []
for i in range(len(n)):
	answer.append(n[i:])
answer.sort()
for i in answer:
	print(i)


