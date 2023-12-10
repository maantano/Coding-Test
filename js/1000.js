const fs = require("fs");
const inputData = fs.readFileSync(0, "utf8").toString().split(" ");
const n1 = parseInt(inputData[0]);
const n2 = parseInt(inputData[0]);

console.log(n1 + n2);

// const fs = require('fs');
// const inputData = fs.readFileSync(0, 'utf8').toString().split(' ');
// const A = parseInt(inputData[0]);
// const B = parseInt(inputData[1]);
// console.log(A+B)
