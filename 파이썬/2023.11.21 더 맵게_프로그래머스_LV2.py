import sys
sys.setrecursionlimit(10**9)
from collections import deque
# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
import heapq

scoville = [1, 2, 3, 9, 10, 12]
K = 7

def solution(scoville, K):
	hq = []
	answer = 0

	for i in scoville:
		heapq.heappush(hq,i)

	while True:
		if hq[0] >= K:
			break
		if len(hq) == 1 and hq[0] < K:
			answer = -1
			break
		mi = heapq.heappop(hq)
		mi2 = heapq.heappop(hq)
		cost = mi + (mi2*2)
		heapq.heappush(hq,cost)
		answer+=1
	return answer

solution(scoville, K)
