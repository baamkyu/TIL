function solution(n, words) {
  // [번호, 차례] 결과값 출력
  let answer = [0, 0];
  
  for (let i = 0; i < words.length; i++) {
    let word = words[i];
    let personNum = i % n + 1;
    let cycleNum = Math.ceil((i + 1)/n);

    if (i > 0) {
      // 이전 단어 마지막 글자
      let last = words[i - 1].split("").pop();

      // 중복이거나 틀린 경우
      if (i > words.indexOf(word) || words[i][0] !== last) {
        answer = [personNum, cycleNum];
        break;
      }
    }
  }

  return answer;
}