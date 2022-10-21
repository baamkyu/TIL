function solution(n) {
    let number = n;
    let index = 1;
    let total = 0;
    while (index <= number) {
        if (number % index === 0) {
            total += index
        }
        index += 1
    }
    return total;
}