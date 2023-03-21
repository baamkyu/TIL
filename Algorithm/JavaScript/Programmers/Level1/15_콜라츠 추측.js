function solution(num) {
  for (let ans=0; ans<500; ans++) {
    if (num % 2 === 0) {
      num = num / 2
    } else if (num === 1) {
      return ans
    } else if (num % 2 === 1) {
      num = (num*3) + 1
    }
  }
  return -1
}