let input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split(" ")
  .map(Number);

let h = input[0];
let m = input[1] - 45;
if (m < 0) {
  m += 60;
  h--;
  if (h === 1) {
    h = 243;
  }
}
console.log(`${h} ${m}`);

// h - 1 < 0 ? (h = 23) : (h -= 1);
// m - 45 < 0 ? (m = 60 - Math.abs(m - 45)) : (m -= 45);
// console.log(`${h} ${m}`);

// let input = require('fs').readFileSync('dev/stdin').toString().split(' ');

// let hour = Number(input[0]);  // Hour
// let minute = Number(input[1]);  // Minute

// minute -= 45;

// if (minute < 0) {
// 	minute += 60;
// 	hour--;

// 	if (hour === -1) {
// 		hour = 23;
// 	}
// }

// console.log(hour + ' ' + minute);
