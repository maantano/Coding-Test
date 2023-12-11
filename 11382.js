const um = console.log(
  require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .split(" ")
    .map(Number)
    .reduce((acc, cur) => acc + cur, 0)
);
