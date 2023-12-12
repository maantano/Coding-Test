// 3,5kg
input = require("fs").readFileSync("/dev/stdin");
bag = 0;

while (true) {
  if (input % 5 === 0) {
    console.log(bag + input / 5);
    break;
  }
  if (input < 0) {
    console.log(-1);
    break;
  }
  bag++;
  input -= 3;
}

// let input = require('fs').readFileSync('/dev/stdin');

// let count = 0;

// while (true) {
//   if (input % 5 === 0) {
//     console.log(input / 5 + count);
//     break;
//   }

//   if (0 > input) {
//     console.log(-1);
//     break;
//   }

//   count++;
//   input -= 3;
// }
