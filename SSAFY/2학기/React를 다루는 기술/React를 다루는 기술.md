# React

# 1. JSX

### 💡 지식 - JSX를 작성할 때는 className으로 스타일을 적용시킨다.

```jsx
JSX를 작성할 때 CSS 클래스를 설정하는 과정에서 className이 아닌 class값을 설정해도 스타일이
적용되기는 합니다. 하지만 그렇게 사용하면 개발자 도구의 Console 탭에 경고가 나타납니다.

이전에는 class로 CSS 클래스를 설정할 때 오류가 발생하고 CSS 클래스가 적용되지 않았는데,
리액트 v16 이상부터는 class를 className으로 변환시켜 주고 경고를 띄웁니다.
```

### 💡 `export` - 모듈 내보내기

```jsx
export default MyComponent;
```

이 코드는 다른 파일에서 이 파일을 import할 때, 위에서 선언한 MyComponent 클래스를 불러오도록 설정합니다.

### 💡 `import` - 모듈 불러오기

```jsx
import React from 'react'
import MyComponent from './MyComponent'

const App = () => {
	return <MyComponent />
}
export default App;
```

import 구문을 사용하여 MyComponent 컴포넌트를 불러옵니다.

### 💡 JSX 내부에서 props 렌더링

```jsx
// MyComponent.js
import React from 'react'

const MyComponent = props => {
	return <div>안녕하세요, 제 이름은 {props.name}입니다.</div>
}
export default MyComponent

// App.js
import React from 'react'
import MyComponent from './MyComponent'

const App = () => {
	return <MyComponent name="React" />
}

export default App
```

⇒ 안녕하세요, 제 이름은 React 입니다. 출력

### 💡 props 기본 값 설정: defaultProps

```jsx
 HeadLine.defaultProps = {
	title: ‘Hello, World’
}

class App extends React.Component {
	render() {
		return <HeadLine />
	}
}
```

### 💡 태그 사이의 내용을 보여주는 children

```jsx
// App.js
import React from 'react'
import MyComponent from './MyComponent'

const App = () => {
	return <MyComponent>리액트</MyComponent>
}
export default App

// MyComponent.js
import React from 'react'

const MyComponent = props => {
	return (
		<div>
			안녕하세요, 제 이름은 { props.name }입니다. <br/>
			children 값은 {props.children}
			입니다.
		</div>
	)
}
MyComponent.defaultProps = {
	name: '기본 이름'
}
export default MyComponent
```

⇒ `안녕하세요, 제 이름은 기본 이름입니다.` 출력

### 💡 isRequired를 사용하여 필수 propTypes 설정

```jsx
// MyComponent.js
import React from 'react'
import PropTypes from 'prop-types'

const MyComponent = ({ name, favoriteNumber, children }) => {
	return (
		<div>
			안녕하세요, 제 이름은 { name }입니다. <br/>
			children 값은 { children }
			입니다.
			<br />
			제가 좋아하는 숫자는 { favoriteNumber }입니다.
		</div>
	)
}
MyComponent.defaultProps = {
	name: '기본 이름'
}

MyComponent.propTypes = {
	name: PropTypes.string,
	favoriteNumber: PropTypes.number.isRequired
}
export default MyComponent

// App.js
import React from 'react'
import MyComponent from './MyComponent'

const App = () => {
	return (
		<MyComponent name="React" favoriteNumber={ 1 }>
			리액트
		</MyComponent>
	)
}
export default App
```

⇒ 안녕하세요, 제 이름은 React입니다.

children 값은 리액트 입니다.

제가 좋아하는 숫자는 1입니다. 출력

# 2. 컴포넌트

### 💡 클래스형 컴포넌트에서 props 사용하기

```jsx
// MyComponent.js
import React, { Component } from 'react'
import PropTypes from 'prop-types'

class MyComponent extends Component {
	render() {
		const { name, favoriteNumber, children } = this.props // 비구조화 할당
		return (
			<div>
				안녕하세요, 제 이름은 { name }입니다. <br/>
				children 값은 { children }
				입니다.
				<br/>
				제가 좋아하는 숫자는 { favoriteNumber }입니다.
			</div>
		)
	}
}

MyCompont.defaultProps = {
	name: '기본 이름'
}

MyComponent.propTypes = {
	name: PropTypes.string,
	favoriteNumber: PropTypes.number.isRequired
}

export default My Component
```

### 💡 클래스형 컴포넌트의 state

```jsx
// Counter.js
import React, { Component } from 'react'

class Counter extends Componen {
	constructor(props) {
		super(props)
		// state의 초기값 설정하기
		this.state = {
			number: 0
		}
	}
	render() {
		const { number } = this.state // state를 조회할 때는 this.state로 조회합니다.
		return (
			<div>
				<h1>{ number } </h1>
				<button
                // onClick을 통해 버튼이 클릭되었을 때 호출할 함수를 지정합니다.
                    onClick = {() => {
                        // this.setState를 사용하여 state에 새로운 값을 넣을 수 있습니다.
                        this.setState({ number: number + 1})
                    }}
                > +1 </button>
            </div>
        )
    }
}
export default Counter;
```

클래스형 컴포넌트에서 constructor를 작성할 때는 반드시 super(props)를 호출해 주어야 합니다.

이 함수가 호출되면 현재 클래스형 컴포넌트가 상속받고 있는 Component 클래스가 지닌 생성자 함수를 호출해 줍니다.

### 💡 함수형 컴포넌트에서 useState 사용하기

배열 비구조화 할당

```jsx
const array = [1, 2]
const [one, two] = array // one = 1, two = 2 할당
```

```jsx
// Say.js
import React, { useState } from 'react'

const Say = () => {
    const [message, setMessage] = useState('')
    const onClickEnter = () => setMessage('안녕하세요!')
    const onClickLeave = () => setMessage('안녕히 가세요!')

    return (
        <div>
            <button onClick={ onClickEnter }>입장</button>
            <button onClick={ onClickLeave }>퇴장</button>
            <h1>{ message }</h1>
        </div>
    )
}

export default Say;
```

useState 함수의 인자에는 상태의 초깃값을 넣어 줍니다.

useState함수에 속한 배열의 첫 번째 원소는 현재 상태이고, 두 번째 원소는 상태를 바꾸어 주는 함수입니다. ⇒ `message = ''`, `setMessage()로 message값을 변경`

### 💡 state를 사용할 때 주의사항

state값을 바꾸어야 할 때는 setState 혹은 useState를 통해 전달받은 세터 함수를 사용해야 합니다.

배열이나 객체를 업데이트 해야 할 때는 배열이나 객체 사본을 만들고 그 사본에 값을 업데이트한 후, 그 사본의 상태를 setState 혹은 세터 함수를 통해 업데이트 합니다.

```jsx
const a = { a: 1, b: 2, c: 3 }
const a2 = {...a, d: 4} // 사본을 만들어서 d값만 덮어 쓰기
```

# 3. 이벤트 핸들링

### 💡 이벤트 사용할 때 주의사항

1. 이벤트 이름은 카멜 표기법으로 작성합니다      ex. onClick, onKeyUp
2. 이벤트에 실행할 자바스크립트 코드를 전달하는 것이 아니라, 함수 형태의 값을 전달합니다.
3. DOM 요소에만 이벤트를 설정할 수 있습니다.
    
    ⇒ div, button, input 등 태그에는 이벤트를 설정할 수 있지만 우리가 직접 만든 컴포넌트에는 이벤트를 자체적으로 설정할 수 없습니다.
    

### 💡 onChange 이벤트 핸들링하기

개발자 도구 Console탭에 입력할 때마다 console.log(입력한 값)이 출력

```jsx
import React, { Component } from 'react'

class EventPractice extends Component {
    render() {
        return (
            <div>
                <h1>이벤트 연습</h1>
                <input
                    type="text"
                    name="message"
                    placeholder="아무거나 입력해 보세요"
                    onChange={
                        (e) => {
                            console.log(e.target.value)
                        }
                    }
                ></input>
            </div>
        )
    }
}
```

state에 input값 담기

```jsx
import React, { Component } from 'react'

class EventPractice extends Component {
    state = {
        message: ''
    }
    render() {
        return (
            <div>
                <h1>이벤트 연습</h1>
                <input
                    type="text"
                    name="message"
                    placeholder="아무거나 입력해 보세요"
                    value = {this.state.message}
                    onChange={
                        (e) => {
                            this.setState({
                                message: e.target.value
                            })
                        }
                    }
                ></input>
            </div>
        )
    }
}
```

버튼을 누르면 alert(’메시지 값’) 출력 후 message값 비우기

```jsx
import React, { Component } from 'react'

class EventPractice extends Component {
    state = {
        message: ''
    }
    render() {
        return (
            <div>
                <h1>이벤트 연습</h1>
                <input
                    type="text"
                    name="message"
                    placeholder="아무거나 입력해 보세요"
                    value = {this.state.message}
                    onChange={
                        (e) => {
                            this.setState({
                                message: e.target.value
                            })
                        }
                    }
                ></input>
                <button onClick = {
                    () => {
                        alert(this.state.message)
                        this.setState({ message: ''})
                    }
                }>메시지 출력 후 값 비우기</button>
            </div>
        )
    }
}
```