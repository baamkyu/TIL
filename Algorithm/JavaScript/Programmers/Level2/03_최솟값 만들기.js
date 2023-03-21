function solution(A,B){
    let ans = 0;
    let a = A.sort((a, b) => a - b)
    let b = B.sort((a, b) => b - a)
    // A는 오름차순, B는 내림차순 정렬 후 계산하면 최소값을 알 수 있음.
    for (let i=0; i<a.length; i++) {
      ans += a[i]*b[i]
    }
    return ans
}