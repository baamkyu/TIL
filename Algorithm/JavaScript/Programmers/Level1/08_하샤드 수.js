function solution(n){
  let numSum = 0;
  let stringNumber = String(n).split('');
  for (let i=0; i < stringNumber.length; i++) {
      numSum += Number(stringNumber[i])
  }
  if (n % numSum == 0) {
    return true
  } else {
    return false
  }
}