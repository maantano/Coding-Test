import sys
input = sys.stdin.readline

today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

def convert(date):
	year,month,day= date.split('.')
	year= int(year) * 12*28
	month= int(month) * 28
	day = int(day)
	return year+month+day

def solution(today,terms,privacies):
	today = convert(today)
	d = {}
	answer = []
	for i in terms:
		a,b = i.split(' ')
		d[a] = 28*int(b)
		d[a] = 28*int(b)
	for j in range(len(privacies)):
		chka,chkb = privacies[j].split(' ')
		if today >= convert(chka) + d[chkb]:
			answer.append(j+1)
	return answer



solution(today,terms,privacies)



# solution(today,terms,privacies)
