# 두 자연수 A와 B가 있을 때, A = BC를 만족하는 자연수 C를 A의 약수라고 한다.
# 예를 들어, 2의 약수는 1, 2가 있고, 24의 약수는 1, 2, 3, 4, 6, 8, 12, 24가 있다.

# 자연수 A의 약수의 합은 A의 모든 약수를 더한 값이고, f(A)로 표현한다.

# x보다 작거나 같은 모든 자연수 y의 f(y)값을 더한 값은 g(x)로 표현한다.

# 자연수 N이 주어졌을 때, g(N)을 구해보자.

# 예제 입력 1
# 1
# 예제 출력 1
# 1
# 예제 입력 2
# 2
# 예제 출력 2
# 4

# 10
# 1 | 1,2 | 1,3 | 1,2,4 | 1,5 | 1,2,3,6 | 1,7 | 1,2,4,8|, 1,3,9 | 1,2,5,10 |
# 87


def getMyDivisor(n):

	divisorsList = []
	for i in range(1, int(n**(1/2)) + 1):
		if (n % i == 0):
			divisorsList.append(i)
			if ( (i**2) != n) :
				divisorsList.append(n // i)
	# divisorsList.sort()
	return sum(divisorsList)


# n = int(input().rstrip())
# cnt = 0

# for i in range(1,n+1):
# 	cnt += getMyDivisor(i)
# print(cnt)

import sys
input=sys.stdin.readline

n = int(input())

sum_ = 0
for i in range(1, n+1):
	sum_ += (n//i)*i

print(sum_)

