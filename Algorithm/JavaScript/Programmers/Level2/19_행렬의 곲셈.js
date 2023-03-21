// 행렬의 곱셈 공식
// https://mathbang.net/562

function solution(arr1, arr2) {
  let answer = [];
  for (let i=0; i<arr1.length; i++) {
    let result = []
    for (let j=0; j<arr2[0].length; j++) {
      let hap = 0;
      for (let k=0; k<arr2.length; k++) {
        hap += arr1[i][k] * arr2[k][j]
      }
      result.push(hap)
    }
    answer.push(result)
  }
  return answer;
}