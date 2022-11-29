// 1. 생성자 함수 : 상품 객체를 생성해보자

function Item(title, price) {
  this.title = title;
  this.price = price;
  this.showPrice = function() {
    console.log(`가격은 ${price}원 입니다.`);
  }
}

const item1 = new Item('인형', 3000);
const item2 = new Item('가방', 4000);
const item3 = new Item('지갑', 9000);

console.log(item1, item2, item3);
// Item { title: '인형', price: 3000, showPrice: [Function (anonymous)] }
// Item { title: '가방', price: 4000, showPrice: [Function (anonymous)] } 
// Item { title: '지갑', price: 9000, showPrice: [Function (anonymous)] }

item3.showPrice(); // 가격은 9000원 입니다.



// 2. 객체 메서드(Object methods), 계산된 프로퍼티(Computed property)
let n = "name";
let a = "age";

const user = {
  [n]: "Mike",
  [a]: 30,
}
console.log(user)