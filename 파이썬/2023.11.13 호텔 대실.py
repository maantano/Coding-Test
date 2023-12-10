
def convert_time(s) :
	sh, sm = map(int, s[0].split(':'))
	eh, em = map(int, s[1].split(':'))
	return [ sh * 60 + sm, eh * 60 + em]


book_time = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]
# book_time =  [["09:10", "10:10"], ["10:20", "12:20"]]
# book_time= [["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]
import heapq

def solution(book_time):
	timeList = []
	answer = 1
	for time in book_time:
		timeList.append(convert_time(time))
	timeList.sort()
	rooms = []
	for s,e in timeList:
		if not rooms:
			heapq.heappush(rooms,e)
			continue

		if rooms[0] <= s:
			heapq.heappop(rooms)
		else:
			answer+=1
		heapq.heappush(rooms,e+10)
	return answer
print(solution(book_time))



# def convert_time(s) :
# 	sh, sm = map(int, s[0].split(':'))
# 	eh, em = map(int, s[1].split(':'))
# 	return [ sh * 60 + sm, eh * 60 + em]


# book_time = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]
# # book_time =  [["09:10", "10:10"], ["10:20", "12:20"]]
# # book_time= [["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]
# def solution(book_time):
# 	timeList = []
# 	answer = 1
# 	for time in book_time:
# 		timeList.append(convert_time(time))
# 	timeList.sort()
# 	# timeList.sort(key=lambda x:( x[1],x[0]))
# 	s,e = timeList[0][0],timeList[0][1]
# 	for i in range(1,len(timeList)):
# 		if timeList[i][0] <= e - 10:
# 			answer+=1
# 		else:
# 			s = timeList[i][0]
# 			e = timeList[i][1]

# 	return answer
# solution(book_time)
