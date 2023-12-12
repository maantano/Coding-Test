let input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .split(" ")
  .trim()
  .map(Number);
function isPrime(num) {
  if (num === 1) {
    return false;
  } else {
    for (let i = 2; i < Math.ceil(num ** 0.5); i++) {
      if (num % i === 0) {
        return false;
      }
    }
    return true;
  }
}

for (let i = input[0]; i <= input[1]; i++) {
  if (isPrime(i)) console.log(i);
}
