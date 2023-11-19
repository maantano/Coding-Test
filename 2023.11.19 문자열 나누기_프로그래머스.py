import sys
input = sys.stdin.readline

s = 'banana'
def solution(s):
	cnt1,cnt2=0,0
	answer = 0
	for i in s:
		if  cnt1 == cnt2:
			answer+=1
			k = i
		if k == i:
			cnt1+=1
		else:
			cnt2+=1
	return answer

print(solution(s))



	# x = dq.popleft()
	# while dq:
	# 	chk = dq.popleft()
	# 	if x == chk:
	# 		same+=1
	# 	else:
	# 		non +=1
	# 	if same == non:
	# 		answer.append(x+chk)
	# 		same = 1
	# 		non = 0
	# 		x = dq.popleft()


