# NextJS

### 1. NextJS란?

생산용 React FrameWork

대규모의 양산형 React 앱을 더 편리하게 구축할 수 잇도록 많은 기능을 제공한다.

### 2. NextJS의 기능

- 서버 사이드 렌더링을 내장하고 있다
    - 서버 사이드 렌더링 : 페이지 콘텐츠를 클라이언트가 아니라 전적으로 서버에서 준비하는 것
    - 자동으로 페이지를 사전 렌더링 함 → 검색 엔진 최적화에 유리함, 초기에 사용자의 화면이 깜빡거리지 않음
- 파일 기반 라우팅
    - React의 라우팅(`<Route path=”/pagename”></Route>`)과는 다르게 NextJS는 파일 기반 라우팅으로 라우팅 간소화가 가능하다
- 풀스택 앱 빌드
    - React 프로젝트에 백엔드API를 쉽게 추가할 수 있다

### 3. Next.js 프로젝트 만들기

- 프로젝트 생성
    
    `npx create-next-app`
    

### 4. 파일 기반 라우팅

- NextJS는 React의 라우팅 방식과는 파일 기반 라우팅을 제공한다. 따라서, 따로 작성할 코드는 없지만 파일 위치가 굉장히 중요하다.
- /, /news, /news/detail, /profile 이라는 페이지구조를 만들어보자.

```jsx
// pages/index.js
function HomePage() {
	return <h1>The Home Page</h1>
}

// pages/news/index.js
function NewsPage() {
	return <h1>The News Page</h1>
}

// pages/news/detail.js
function DetailPage() {
	return <h1>The Detail Page</h1>
}

// pages/profile.js 혹은 pages/profile/index.js
function HomePage() {
	return <h1>The Profile Page</h1>
}
```
- NextJS에서 제공하는 hook을 이용한 동적 매개변수 값 추출하기

```jsx
// pages/news/[newsId].js
import { useRouter } from 'next/router'

function DetailPage() {
	const router = useRouter()

	const newsId = router.query.newsId
	console.log(router.query.newsId). 

	return <h1>The Detail Page</h1>
}
```

입력 후 /news/anything 이라는 주소를 들어가면 콘솔에 anything이라고 찍혀있을 것이다.

### 5. SPA 라우팅

- <a> tag에 href 속성으로 링크를 이동할 수 있다. 하지만 이 방식으로 사용하게 되면 SPA가 아닌 새로운 url을 요청해 새로운 페이지를 렌더링 하게 된다. 이를 보완하고자 NextJS에서 제공하는 Link 컴포넌트를 활용하면 된다.

```jsx
import Link from 'next/link'

function NewsPage() {
	return (
		<Fragment>
			<Link href='news/anything'>Clicked To Go Anything Page</Link>
		</Fragment>
	)
}
```