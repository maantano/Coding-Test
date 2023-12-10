import sys
input = sys.stdin.readline


n = int(input())
info = [0 for _ in range(1001)]
max_high = 0
max_high_idx = 0
end_idx = 0

for i in range(n):
	w,h = map(int,input().split())
	info[w] = h
	if max_high < h:
		max_high = h
		max_high_idx = w
	end_idx = max(end_idx,w)

stack = []
area = 0

for i in range(0,max_high_idx+1):
	if not stack:
		stack.append(info[i])
	else:
		if stack[-1] < info[i]:
			stack.append(info[i])
	area += stack[-1]
stack = []

for i in range(end_idx,max_high_idx,-1):
	if not stack:
		stack.append(info[i])
	else:
		if stack[-1] < info[i]:
			stack.append(info[i])
	area+= stack[-1]
print(area)







# n = int(input())
# rec = [0 for _ in range(1001)]
# for _ in range(n):
# 	l,h = map(int,input().split())
# 	rec[l] = h
# max_idx = rec.index(max(rec))
