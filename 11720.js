// const input = require("fs").readFileSync("/dev/stdin").toString().split("\n");
// const n = input[0];
// const chk = input[1].split("");
// console.log(chk.reduce((acc,cur)=>acc+Number(cur),0))

let n = 5;
let chk = "54321";
const l = chk.split("");
console.log(l);
console.log(l.reduce((acc, cur) => acc + Number(cur), 0));
