function solution(arr){
    let hap = 0;    // datatype 설정
    for (let num of arr) {
        hap += num
    }
    let ans = hap / arr.length
    return ans;
}
