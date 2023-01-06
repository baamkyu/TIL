function solution(n,a,b) {
  let answer = 1;

  while (Math.pow(2, answer) < n) {
      if (Math.abs(a-b) == 1 && Math.min(a, b) % 2 == 1) {
          break;
      }
      
      a = Math.ceil(a / 2);
      b = Math.ceil(b / 2);
      
      ++answer;
  }
  
  return answer;
}