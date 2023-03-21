function solution(s) {
  let deleteZero = 0 // 삭제한 0의 개수
  let count = 0 // 이진수로 변환한 횟수
  while(s.length !== 1){
      const originLen = s.length
      s = s.split('').filter(v=>v === '1').join('')
      const len = s.length
      deleteZero += originLen-len
      s = len.toString(2)
      count++
  }
  return[count, deleteZero]
}