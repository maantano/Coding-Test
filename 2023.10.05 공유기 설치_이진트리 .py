import sys
input = sys.stdin.readline

n, c = map(int, input().split())
house = sorted([int(input()) for _ in range(n)])

max_diff = house[-1] - house[0]
start, end = 1, max_diff
answer = 0

while start <= end:
    mid = (start + end) // 2 # 현재 기준 간격
    current = house[0] # 현재 기준 집 위치
    count = 1 # 공유기 설치 개수
    diff = max_diff

    for i in range(1, n): # 공유기 사이의 간격이니까 1 ~ n-1
        if house[i] - current >= mid: # 간격이 기준 보다 넓으면 공유기 설치
            diff = min(diff, house[i] - current)
            count += 1
            current = house[i]
    if count >= c: # 공유기 모두 설치 가능, 간격 늘림
        start = mid + 1
        answer = max(answer, diff)
    else: # 공유가 모두 설치 불가, 간격 좁힘
        end = mid - 1
print(answer)
