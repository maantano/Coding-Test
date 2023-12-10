import sys
input = sys.stdin.readline

n,m = map(int,input().split())

a1 = set(([str(input().rstrip()) for _ in range(n)]))
a2 = set([str(input().rstrip()) for _ in range(m)])

print(len(sorted(list(a1-(a1 - a2)))))
for i in sorted(list(a1-(a1 - a2))):
	print(i)
