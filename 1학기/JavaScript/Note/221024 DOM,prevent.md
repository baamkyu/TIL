# 221024

# DOM

## DOM 조작 순서

1. 선택
2. 조작

### 선택 method

`document.querySelector(selector)`

: selector를 만족하는 첫 번째 element를 반환

`document.querySelectorAll(selector)`

: selector를 만족하는 모든 element를 반환 (NodeList로 반환)

### 조작 method

> 생성
> 

`document.createElement(tagName)`

> 입력
> 

`Node.innerText`

> 추가
> 

`Node.appendChild()`

> 삭제
> 

`Node.removeChild()`

### 조작 method - 속성 조회 및 설정

> 속성 조회
> 

`Element.getAttribute(attributeName)`: attributeName의 속성을 조회

> 속성 값 설정
> 

`Element.setAttribute(name, value)`: name속성에 value값을 지정

이미 존재하는 속성이라면 값을 갱신

# EVENT

> 특정 Event에만 함수 작동
> 

`addEventListener(type, lister[, options])` 

: 지정한 Event가 대상에 전달될 때마다 호출할 함수를 설정

- type : 반응할 Event 유형 → ex. input, click, submit 등 ….
- listener : 콜백 함수

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <style>
      .blue {
        color: blue;
      }
    </style>
  </head>
  <body>
    <h1></h1>
    <button id="btn">클릭</button>
    <input type="text" />

    <script>
      // 버튼을 클릭했을 때 파란색으로 된다
      const btn = document.querySelector("#btn");
      btn.addEventListener("click", function (event) {
        const h1Tag = document.querySelector("h1");
        h1Tag.classList.toggle("blue");
      });

      // h1태그에 그대로 입력되는거
      const inputTag = document.querySelector("input");
      inputTag.addEventListener("input", function (event) {
        const h1Tag = document.querySelector("h1");
        h1Tag.innerText = event.target.value;
      });
    </script>
  </body>
</html>
```

> 특정 event의 동작을 막는 함수
> 

`event.preventDefault()` : Event의 동작을 작동하지 않게 막음