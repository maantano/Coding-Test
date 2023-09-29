import sys
n, m = map(int, sys.stdin.readline().split())


stack = []
cnt = {}

for i in range(n):
	tmp = sys.stdin.readline().rstrip()
	if len(tmp) < m:
		continue
	if not cnt.get(tmp):
		cnt[tmp] = 1
	else:
		cnt[tmp] += 1

wordL = cnt.keys()
wordL = sorted(wordL,key=lambda x : (-cnt[x],-len(x),x))

for i in wordL:
	print(i)
# stack = list(set(stack))
# stack.sort()
# stack.sort(key=lambda x : (x,len(x),x))



