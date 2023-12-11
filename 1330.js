input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .split("")
  .trim()
  .map(Number);
input[0] > input[1] ? console.log(">") : console.log("<");
