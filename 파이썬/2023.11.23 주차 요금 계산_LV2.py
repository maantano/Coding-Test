# fees = [180, 5000, 10, 600]
# records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
# result = [14600, 34400, 5000]

# fees = [120, 0, 60, 591]
# records = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]
# result = [0, 591]

fees = [1, 461, 1, 10]
records =  ["00:00 1234 IN"]



# print(convert('00:00','IN'))
# print(convert('23:49','OUT'))
# print(convert("06:34","OUT"))
# print(convert("18:59",'IN'))
# print(convert('23:59','OUT'))
# print(convert('06:00','IN')+
# convert("06:34","OUT")+
# convert("18:59",'IN')+
# convert('23:59','OUT'))
# print(fees[1]+math.ceil((334-fees[0]) / fees[2]) * fees[3])

import math
def convert(time,flag):
	t,m= time.split(':')
	return ((int(t)*60) + int(m)) *  (-1 if flag == 'IN' else 1)

def solution(fees, records):
	answer = []
	d = {}
	for i in records:
		time,number,flag= i.split(' ')
		if number not in d:
			d[number] = convert(time,flag)
		else:
			d[number] += (convert(time,flag))

	for carNo,time in d.items():

		if time <= 0:
			time+=convert("23:59",'OUT')
		if time < fees[0]:
			d[carNo] = fees[1]
		else:
			d[carNo] = fees[1] + math.ceil(((time-fees[0]) / fees[2])) * fees[3]
	return list(map(lambda x : x[1], sorted(result.items())))
	# for i in sorted(d.items()):
	# 	answer.append(i[1])

	# return answer

# def solution(fees, records):
# 	answer = []
# 	d = {}
# 	for i in records:
# 		time,number,flag= i.split(' ')
# 		if number not in d:
# 			d[number] = convert(time,flag)
# 		else:
# 			d[number] += (convert(time,flag))

# 	for carNo,time in d.items():
# 		# print(carNo,time)
# 		if time < 0:
# 			time+=convert("23:59",'OUT')
# 		if time < fees[0]:
# 			answer.append([carNo,fees[1]])
# 		else:
# 			answer.append([carNo,fees[1] + math.ceil(((time-fees[0]) / fees[2])) * fees[3]])

# 	print(answer.sort(key=lambda x: x[0]))


# 	return answer

solution(fees, records)
# print(convert('05:34',1))
