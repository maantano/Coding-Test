# 스테이지에 도달했으나 아직 클리어하지 못한 플에이어의 수 / 스테이지에 도달한 플레이어의 수

# 전체 스테이지의 개수 : N
# 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질때
# 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담긴 배열을 리턴 하시오

n = 5
stages = [2,1,2,6,2,4,3,3]
# result = [3,4,2,1,5]


def solution(n,stages):
	p = len(stages)
	d = {}

	for i in range(1,n+1):
		if p != 0:
			d[i] = stages.count(i) / p
			p -= stages.count(i)
		else:
			d[i] = 0
	return sorted(d,key=lambda x : d[x],reverse=True)


solution(n,stages)

