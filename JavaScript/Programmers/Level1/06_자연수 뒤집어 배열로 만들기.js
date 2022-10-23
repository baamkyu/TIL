function solution(n) {
  return String(n)
    .split('') // 리스트로 나눠줌 -> ['1', '2', '3', '4', '5']
    .reverse() // 순서를 바꿔줌 -> ['5', '4', '3', '2', '1']
    .map((x) => parseInt(x)); // int형으로 바꿔줌 -> [5, 4, 3, 2, 1]
  }