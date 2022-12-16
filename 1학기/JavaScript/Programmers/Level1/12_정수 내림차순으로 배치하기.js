function solution(n) {
  let num = n + ''
  let answer = num.split('')
  return Number(answer.sort((a, b) => b - a).join(''))
}