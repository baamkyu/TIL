// 원하는 부분부터 가져오기
let list = [
  "01. 생성자함수",
  "02. 객체메서드 & 계산된 프로퍼티",
  "03. 심볼",
  "04. 숫자 & 수학",
  "05. String",
];

let newList = [];

for (let i = 0; i < list.length; i++) {
  newList.push(list[i].slice(4));
}

console.log(newList)



// 금칙어 : 콜라
// indexOf 사용
function hasCola(str) {
  if(str.indexOf('콜라') > -1) {
    console.log('금칙어가 있습니다.');
  } else {
    console.log('통과')
  }
}

hasCola('사이다가 짱이야!');
hasCola('콜라가 최고야!');
hasCola('콜라');

// 금칙어 : 콜라
// includes 사용
function hasCola2(str) {
  if(str.includes('콜라')) {
    console.log('금칙어가 있습니다.');
  } else {
    console.log('통과');
  }
}
hasCola2('사이다가 짱이야!');
hasCola2('콜라가 최고야!');
hasCola2('콜라');