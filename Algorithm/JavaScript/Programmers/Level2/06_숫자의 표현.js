// 로직 : 첫번째 수를 정하고 그 수부터 차례대로 더한다
// if 더한 수 === n이 되면 ans += 1
// else if 더한 수 > n이 되면 sumNow = 0, firstNum++해서 다시 시작
// else (더한 수 < n) 인 경우, nowNum++

function solution(n) {
  let ans = 0; // 합이 n이 되는 경우의 수
  let sumNow = 0; // 현재까지 더한 수
  let nowNum = 1; // 현재 수
  let firstNum = 1; // 더하기 시작한 첫번째 수

  while (firstNum <= n) {
    sumNow += nowNum
    if (sumNow === n) {
      ans++
      sumNow = 0
      firstNum++
      nowNum = firstNum
    } else if (sumNow > n) {
      sumNow = 0
      firstNum++
      nowNum = firstNum
    } else {
      nowNum++
    }
  }
  return ans
}


//     sumNow += nowNum
//     if (sumNow >= n) {
//       if (sumNow === n) {
//         sumNow = 0
//         ans ++
//         firstNum++
//       }
//     } else nowNum++
//   }
// }