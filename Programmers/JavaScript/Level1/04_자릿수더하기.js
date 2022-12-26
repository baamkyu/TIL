function solution(n){
    let answer = 0;
    let stringNumber = n.toString()
    for (let i=0; i < stringNumber.length; i++) {
        answer += parseInt(stringNumber[i])
    }
    return answer
}

console.log(solution(15))