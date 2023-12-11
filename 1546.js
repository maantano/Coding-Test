// let input = require('fs').readFileSync('/dev/stdin').toString().split('\n')
// let n = input[0]
// let l = input[1].split('')

n = 3;
l = "40 80 60".split(" ").map(Number);

l.sort((a, b) => b - a);
let total = l.reduce((acc, cur) => acc + cur, 0);
let maxNum = l[0];
console.log((total / maxNum) * 100);
// console.log(l.reduce((acc, cur) => acc + Number(cur), 0));
// console.log((l.reduce((acc, cur) => acc + Number(cur)), 0) / n);
