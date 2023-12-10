import sys
input = sys.stdin.readline


cap = 4
n = 5
deliveries = [1, 0, 3, 1, 2]
pickups = [0, 3, 0, 4, 0]


def solution(cap, n, deliveries, pickups):
	answer=  0

	deliveries = deliveries[::-1]
	pickups = pickups[::-1]

	to_d = 0
	to_p = 0

	for i in range(n):
		to_d += deliveries[i]
		to_p += pickups[i]


		while to_d > 0 or to_p > 0:
			to_p -= cap
			to_d -= cap
			answer += (n-i) * 2

	return answer
solution(cap, n, deliveries, pickups)
