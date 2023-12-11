// let input = require("fs").readFileSync("/dev/stdin").split(" ").map(Number);

// let h = input[0];
// let m = input[1];
h = 0;
m = 30;

h - 1 < 0 ? (h = 23) : (h -= 1);
m - 45 < 0 ? (m = 60 - Math.abs(m - 45)) : (m -= 45);

console.log(`${h} ${m}`);
