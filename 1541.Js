// const fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString().split("-");
// const [front, back] = input;
// if (!back) {
//   console.log(0);
// } else {
//   let frontArr = front.split("+");
//   let backArr = back.split("+");
//   let answer = 0;
//   for (let i = 0; i < frontArr.length; i++) {
//     answer += Number(frontArr[i]);
//   }
//   for (let j = 0; j < backArr.length; j++) {
//     answer -= Number(backArr[j]);
//   }
//   console.log(answer);
// }

const fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("-");
const [front, back] = input;
if (!back) {
  console.log(0);
} else {
  let frontArr = front.split("+");
  let backArr = back.split("+");
  let answer = 0;
  for (let i = 0; i < frontArr.length; i++) {
    answer += Number(frontArr[i]);
  }
  for (let j = 0; j < backArr.length; j++) {
    answer -= Number(backArr[j]);
  }
  console.log(answer);
}
