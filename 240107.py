# 14889 스타트와 링크

n = int(input())
arr = [list(map(int,input().split(' '))) for _ in range(n)]


def chk(idx,first,second):
	if idx == n:
		if len(first) != n/2:
			return -1
		if len(second) != n/2:
			return -1
		t1 = 0
		t2 = 0
		for i in range(n//2):
			for j in range(n//2):
				if i == j:
					continue
				t1 += arr[first[i]][first[j]]
				t2 += arr[second[i]][second[j]]
		diff = abs(t1 - t2)
		return diff
	ans = -1
	t1 = chk(idx+1,first+[idx],second)
	if ans == -1 or (t1 != -1 and ans>t1):
		ans = t1
	t2 = chk(idx+1,first,second+[idx])
	if ans == -1 or (t2 != -1 and ans > t2):
		ans = t2
	return ans

print(chk(0,[],[]))
