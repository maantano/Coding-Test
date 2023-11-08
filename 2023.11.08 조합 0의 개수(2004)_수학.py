N, M = map(int, input().split())

def count_number(n, k):
	count = 0
	while n:
		n //= k
		count += n
	return count


five_count = count_number(N, 5) - count_number(M, 5) - count_number(N - M, 5)
two_count = count_number(N, 2) - count_number(M, 2) - count_number(N - M, 2)

answer = min(five_count, two_count)
print(answer)



# def two_count(n):
# 	two = 0
# 	while n != 0:
# 		n = n // 2
# 		two += n
# 	return two
# 여기서 알수있는것이 먼저 8 7 6 5 4 3 2 1에서 2의 배수의 갯수를 구한다. 8/2 = 4

# 다음으로 제곱수에 대해서 배수를 구한다. 8/(2*2) = 2

# 다음으로 세제곱수에 대해서 배수를 구한다. 8/(2*2*2) = 1

# 즉 4 + 2 + 1이란 것이다.



# 한번더 100으로 예시를 들면....

# 100!을 생각해 봤을 때, 5가 곱해진 개수를 구해해보자.

# 일단 100까지의 수 중에서 5의 배수들이 5를 1개씩 가지고 있음을 알고 있다.

# 100까지의 5의 배수는 20개 이므로 100/5=20을 먼저 구한다.( 5, 10, 15, 20, 25 ... 100 이는 5를 1개이상씩 가지고있다 )

# 여기서 5의 지수가 2인 애들을 보면 5^2의 배수들(25, 50, 75, 100)이 5를 하나씩 더 가지고 있음(2개)을 알 수 있다

# 따라서 기존에 20에다가 100/5^2=4 를 더해준다.
