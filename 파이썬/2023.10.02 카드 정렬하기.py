n = int(input())
import heapq
h = []
for i in range(n):
	data = int(input())
	heapq.heappush(h,data)


result = 0
while len(h) != 1:
	one = heapq.heappop(h)
	two = heapq.heappop(h)
	sumV = one +two
	result += sumV
	heapq.heappush(h,sumV)
print(result)



