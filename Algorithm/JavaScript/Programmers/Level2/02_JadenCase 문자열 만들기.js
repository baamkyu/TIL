function solution(s) {
    var word = s.toLowerCase().split(' ')
    var ans = word.map((v) => v.charAt(0).toUpperCase() + v.substring(1)) // 첫번째 글자만 대문자로 변환하고 그 뒤에 1번 인덱스~끝 인덱스 까지 붙여줌
    var ans2 = ans.join(' ')
    return ans2
}