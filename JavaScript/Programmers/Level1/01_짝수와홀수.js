function solution(num) {
  if (num % 2 === 0) {
    var ans = "Even";
  } else {
    var ans = "Odd";
  }
  return ans;
}

console.log(solution(10))