import sys
input = sys.stdin.readline

# n = 8
# m = 4
# section =[2,3,6]

# n = 5
# m = 4
# section =[1,3]

n = 4
m = 1
section =[1,2,3,4]


### 실패
def solution(n,m,section):
	answer = 0
	arr = [1] * (n)
	for i in section:
		arr[i-1] = 0
	for i in range(n-m+1):
		if 0 in arr[i:i+m]:
			for j in range(m):
				arr[i+j] = 1
			answer+=1
	return answer


solution(n,m,section)

### 성공
def solution(n, m, section):
	answer = 1
	paint = section[0]
	for i in range(1, len(section)):
		if section[i] - paint >= m:
			answer += 1
			paint = section[i]

	return answer
