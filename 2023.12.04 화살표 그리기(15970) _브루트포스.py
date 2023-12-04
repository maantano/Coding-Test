import sys
input = sys.stdin.readline

def distance(s):
	leng = 0
	for i in range(len(s)):
		if i == 0:
			leng += abs(s[i] - s[i+1])
		elif i == len(s)-1:
			leng += abs(s[i]-s[i-1])
		else:
			leng += min(abs(s[i]-s[i+1]),abs(s[i]-s[i-1]))
	return leng


n = int(input())
answer = 0
arr = []
for i in range(n):
	loc,color = map(int,input().split())
	arr.append((color,loc))
arr.sort()

num_color = arr[-1][0]

for i in range(1,num_color+1):
	same_color = []
	for j in range(n):
		if arr[j][0] == i:
			same_color.append(arr[j][1])
	answer += distance(same_color)
print(answer)
