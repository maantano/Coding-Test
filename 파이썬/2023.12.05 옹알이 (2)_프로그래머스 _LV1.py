import sys
input = sys.stdin.readline
from itertools import permutations



babbling = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]
def solution(babbling):
	chk = ["aya", "ye", "woo", "ma"]
	s = set();
	cnt = 0
	for i in range(1,len(chk)+1):
		for j in permutations(chk,i):
			s.add(''.join(j))
	for m in chk:
		if (m*2) in s:
			s.remove(m*2)
	for k in babbling:
		if k in s:
			cnt+=1
	return cnt
solution(babbling)

# {'yewoo', 'ayaye', 'ayawooye', 'yewooayama', 'ayamaye', 'yemawooaya', 'woomaaya', 'maye', 'woomaye', 'yewooma', 'maayawooye', 'ayawooyema', 'wooyema', 'mawooyeaya', 'wooyeaya', 'yewooaya', 'mawooaya', 'mayewooaya', 'ayawoomaye', 'ayamayewoo', 'maayayewoo', 'wooyeayama', 'woomaayaye', 'wooayamaye', 'yemawoo', 'ayamawooye', 'wooyemaaya', 'ayama', 'ayayema', 'ayayewooma', 'ayayemawoo', 'yema', 'mayeayawoo', 'aya', 'maayaye', 'ayawoo', 'wooayama', 'yeayama', 'mawoo', 'ma', 'yeaya', 'wooayaye', 'maayawoo', 'wooma', 'wooye', 'ye', 'yemaayawoo', 'woomayeaya', 'yeayamawoo', 'mawooayaye', 'ayamawoo', 'ayawooma', 'yewoomaaya', 'mawooye', 'maaya', 'wooayayema', 'ayayewoo', 'mayeaya', 'yeayawoo', 'woo', 'yeayawooma', 'yemaaya', 'mayewoo', 'wooaya'}
