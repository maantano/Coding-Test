import sys

n = input().rstrip()
chk = input().rstrip()



idx = 0
answer= 0
while True:
	if idx > len(n):
		break
	if n[idx:idx+len(chk)] == chk:
		idx += len(chk)
		answer +=1
	else:
		idx += 1
print(answer)

print(len(n.split(chk))-1)

# import sys
# S = sys.stdin.readline().strip()
# x = sys.stdin.readline().strip()
# i = 0
# cnt = 0
# while i < len(S):
# 	if S[i:i+len(x)] == x:
# 		i += len(x)
# 		cnt += 1
# 	else :
# 		i += 1
# print(cnt)
