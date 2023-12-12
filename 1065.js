// 한수

// def hansu(num) :
// 	hansu_cnt = 0
// 	for i in range(1, num+1):
// 		num_list = list(map(int,str(i)))
// 		if i < 100:
// 			hansu_cnt += 1  # 100보다 작으면 모두 한수
// 		elif num_list[0]-num_list[1] == num_list[1]-num_list[2]:
// 			hansu_cnt += 1  # x의 각 자리가 등차수열이면 한수
// 	return hansu_cnt

// num = int(input())
// print(hansu(num))

// num = int(input())

// hansu = 0
// for i in range(1, num+1):
// 	num_list = list(map(int, str(i)))
// 	if i < 100:
// 		hansu += 1  # 100보다 작으면 모두 한수
// 	elif num_list[0]-num_list[1] == num_list[1]-num_list[2]:
// 		hansu += 1  # x의 각 자리가 등차수열이면 한수
// print(hansu)

input = Number(require("fs").readFileSync("/dev/stdin"));
function hansu(n) {
  let cnt = 0;
  tmpList = [];

  for (let i = 1; i <= n; i++) {
    tmpList = String(i);

    if (i < 100) {
      cnt++;
    } else if (
      Number(tmpList[0]) - Number(tmpList[1]) ==
      Number(tmpList[1]) - Number(tmpList[2])
    ) {
      cnt++;
    }
  }
  return cnt;
}
console.log(hansu(input));
