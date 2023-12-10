
import sys

n = input()

if '0' not in n:
	print(-1)
else:
	num_sum = 0

	for i in range(len(n)):
		num_sum+= int(n[i])

	if num_sum % 3 != 0:
		print(-1)

	else:
		sortNum = sorted(n,reverse=True)
		answer = ''.join(sortNum)
		print(answer)
