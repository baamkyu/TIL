function solution(n){
  for (i=0; i<=n; i++){
    if (n==i**2){
      return (i+1)**2 // 어떤 수의 제곱근이면 그 수 +1의 제곱을 return
    }
  }
  return -1 // if문 로직이 실행 안 하면 여기까지 옴
}