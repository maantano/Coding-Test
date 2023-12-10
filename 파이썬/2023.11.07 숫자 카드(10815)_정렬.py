import sys
input = sys.stdin.readline

n = int(input())
a1 = list(map(int,input().split()))
m = int(input())
a2 = list(map(int,input().split()))

d1 = {v:1 for idx,v in enumerate(a1)}
d2 = {v:0 for idx,v in enumerate(a2)}

for key,cnt in d1.items():
	if key in d2:
		d2[key] += 1
print(*d2.values(),sep=' ')



