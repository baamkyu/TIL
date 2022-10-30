function solution(s){
  let p_cnt = 0
  let y_cnt = 0
  for (let string of s) {
    if (string === 'p' || string ==='P') {
      p_cnt += 1
    } else if (string === 'y' || string === 'Y') {
      y_cnt += 1
    }
  }

  var answer = true;
  if (p_cnt != y_cnt) {
    answer = false;
  }
  return answer;
}