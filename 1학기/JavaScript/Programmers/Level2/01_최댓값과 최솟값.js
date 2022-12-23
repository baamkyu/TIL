function solution(s) {
    let centence = s.split(" ")
    let max = Math.max(...centence)
    let min = Math.min(...centence)
    return min+" "+max;
}