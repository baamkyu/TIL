function solution(arr) {
  if (arr.length <= 1) {
    return [-1]
  } else {
    let minNum = Math.min(...arr);
      let minNumidx = arr.indexOf(minNum)
      arr.splice(minNumidx, 1);
      return arr
  }
}