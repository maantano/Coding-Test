// 예를 들어, 2012년은 4의 배수이면서 100의 배수가 아니라서 윤년이다.
// 1900년은 100의 배수이고 400의 배수는 아니기 때문에 윤년이 아니다.
// 하지만, 2000년은 400의 배수이기 때문에 윤년이다.

input = 2012;
input = parseInt(require("fs").readFileSync("/dev/stdin"));
chk = false;
if (input % 4 == 0 && input % 100 != 0) {
  chk = true;
} else if (input % 100 == 0 && input % 400 != 0) {
  chk = false;
}

if (input % 400 == 0) {
  chk = true;
}

chk === true ? console.log(1) : console.log(0);
