
data= [[2,2,6],[1,5,10],[4,2,9],[3,8,3]]
col=2
row_begin = 2
row_end = 3
# result = 4

def solution(data, col, row_begin, row_end):
	# data.sort(key=lambda x : (x[col-1],-x[0]))
	answer = 0
	data = sorted(data,key=lambda x : (x[col-1],-x[0]))
	for i in range(row_begin,row_end+1):
		total = 0
		for j in data[i-1]:
			total += (j % i)
		answer ^= total
	return answer

solution(data, col, row_begin, row_end)
