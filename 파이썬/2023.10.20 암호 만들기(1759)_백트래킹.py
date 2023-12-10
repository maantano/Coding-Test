import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = list(map(str,input().split()))
arr.sort()
# arr = sorted(list(map(str,input().split())))

vowel = ['a','e','i','o','u']
answer = []

def bt(cnt,idx):
	if cnt == n:
		vo,co = 0,0
		for i in range(n):
			if answer[i] in vowel:
				vo+=1
			else:
				co+=1
		if vo >= 1 and co >= 2:
			print("".join(answer))
		return
	for i in range(idx,m):
		answer.append(arr[i])
		bt(cnt+1,i+1)
		answer.pop()
bt(0,0)


