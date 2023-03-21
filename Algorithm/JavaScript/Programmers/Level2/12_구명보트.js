function solution(people, limit) {
  let answer = 0;
  people.sort((a, b) => b - a) // 오름차순 정렬
  let highWeight = people.length - 1 // 가장 무거운 사람의 인덱스

  // 가장 가벼운 사람 + 가장 무거운 사람이 탈 수 있으면 태움
  // 탈 수 없으면 가장 가벼운 사람만 태워서 보냄
  
  for (let i=0; i<=highWeight; i++) {
    answer++
    if (people[i] + people[highWeight] <= limit) {
      highWeight--
    }
  } 
  return answer
}