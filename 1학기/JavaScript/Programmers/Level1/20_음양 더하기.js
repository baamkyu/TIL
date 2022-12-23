function solution(absolutes, signs) {
  let ans = 0;
  for (i=0; i<signs.length; i++) {
    if (signs[i] === true) {
      ans += absolutes[i]
    } else {
      ans -= absolutes[i]
    }
  } return ans
}