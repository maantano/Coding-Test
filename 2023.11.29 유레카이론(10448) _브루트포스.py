import sys
input = sys.stdin.readline

arr = [int(input()) for _ in range(10)]

sum_num = 0
idx = 0
answer = []
for i in range(len(arr)):
	tmp = arr[i]
	print(arr[i])
	for j in range(i+1,len(arr)):
		print(arr[j])

		tmp+=arr[j]
		if tmp >= 100:
			pre = 0
			if abs(tmp-100) <= abs(tmp-arr[j]-100):
				answer.append(tmp)
			else:
				answer.append(100 - tmp-arr[j])
			break
	print('tmp ===>',tmp)
	print('---------------------')
print(answer)
# 	sum_num+=arr[i]
# 	idx = i
# 	if sum_num > 100:
# 		break
# print(sum_num)
# print(idx)


import sys
input = sys.stdin.readline

m = []
score = 0
for i in range(10):
	m.append(int(input()))
for j in m:
	score += j
	if score >= 100:
		if score - 100 > 100 - (score - j):
			score -= j
		break
print(score)

score = 0
mushrooms = []
for _ in range(10):
	mushrooms.append(int(input()))

for i in range(10):
	ex_score = score
	score += mushrooms[i]
	if score >= 100:
		under = 100 - ex_score
		over = score - 100
		if over <= under:
			print(score)
			break
		else:
			print(ex_score)
			break
else:
	print(score)
