# typescript_basis

## 1. 타입스크립트란 무엇인가?

자바스크립트에서 확장된 언어로, 자바스크립트에 타입을 부여한 언어이다.

자바스크립트의 기본적인 문법들과 코드 작성법, if문, for문, 객체 사용법 등을 그대로 사용한다.

다만, 타입스크립트는 자바스크립트의 문법에 몇 가지 기능이 추가된다.

첫 번째로, **정적 타입(Static Type)**의 특징을 갖는다.

```jsx
// 1. 자바스크립트 (동적 타입)
function add (a, b) {
	console.log(a + b);
}

add(1) // NaN
add(1, 2) // 3
add('1', '2') // 12
```

```tsx
// 2. 타입스크립트 (정적 타입)
function add(a: number, b: number){
	return a + b;
}

add(1) // 오류
add(1, 2) // 3
add (1, 2, 3) // 오류
add('1', '2') // 오류
```

### 타입스크립트를 사용하는 이유

- 위의 예제처럼 타입스크립트는 **에러를 사전에 방지**할 수 있고 **의도하지 않은 코드의 동작을 방지**할 수 있다.
- 코드 자동 완성과 가이드
    
    Visual Studio Code와 같은 개발 툴의 기능을 최대로 활용할 수 있다.
    
    위와 같은 예시에서 함수의 결괏값을 이용해 코드를 작성해야 하는 상황이 발생할 수 있다.
    
    이때 개발자는 함수의 결과를 예상하고 그 타입을 `number`라고 가정한 상태에서 코드를 작성할 것이다.
    
    자바스크립트는 이러한 경우에도 결괏값의 타입이 `number`인 것을 인지하지 못한다.
    
    하지만 타입스크립트는 타입을 인지하고 그 타입에 대한 API를 미리 보기로 띄워주고, 빠르고 정확하게 코드를 작성할 수 있다.
    

# 2. 타입스크립트 설치 및 사용법

### 타입스크립트 설치

`npm init -y` : package.json 생성

`npm install typesciprt`

### 타입스크립트 컴파일

`npx tsc 파일명`

### **타입스크립트 공식문서 한글버전**

[Handbook - The TypeScript Handbook](https://www.typescriptlang.org/ko/docs/handbook/intro.html)