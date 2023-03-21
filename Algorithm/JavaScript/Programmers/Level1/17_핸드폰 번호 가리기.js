function solution(phone_number) {
  let ans = ''
  for (i=0; i<phone_number.length; i++) {
      if (i < phone_number.length - 4) {
          ans = ans + '*'
    } else {
        ans = ans + phone_number[i]
    }}
    return ans
}