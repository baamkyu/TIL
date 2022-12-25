function solution(arr, divisor) {
  let ans = []
  for (i=0; i<arr.length; i++) {
    if (arr[i] % divisor === 0) {
      ans.push(arr[i])
    }
  }
  if (ans.length === 0) {
    return [-1]
  } else {
    return ans.sort((a, b) => a - b);
  }
}