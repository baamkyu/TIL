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

- a tag에 href 속성으로 링크를 이동할 수 있다. 하지만 이 방식으로 사용하게 되면 SPA가 아닌 새로운 url을 요청해 새로운 페이지를 렌더링 하게 된다. 이를 보완하고자 NextJS에서 제공하는 Link 컴포넌트를 활용하면 된다.

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

### 6. NextJS에 내장된 페이지 사전 렌더링 기능
- 라우터 → (요청) → 페이지에 사전 렌더링한 페이지 반환해서 출력 = 데이터 손실

이러한 경우 데이터가 손실된 상태가 된다

단점: 사전 렌더링한 페이지는 컴포넌트가 첫번째 렌더링 사이클을 마친 이후의 데이터를 콘텐츠로 갖는다

초기에 반환된 HTML 코드에 데이터가 포함되도록 데이터가 있는 페이지를 사전 렌더링하려면 내장된 사전 렌더링 프로세스를 조정해야 한다

### How?

1. 정적 생성
    
    사전렌더링이 되는 시점은 프로젝트가 빌드되는 시점이다. (npm run build 할 때)
    
    데이터를 업데이트 했는데 렌더링한 페이지를 변경해야 한다면 해당 빌드 프로세스를 다시 시작해야하고 다시 배포해야한다. (로컬 껐다가 다시 켜야함)
    
    하지만 이러한 경우 페이지 컴포넌트 파일 안에서 getStaticProps()라는 함수를 export로 내보내면 된다. → `export function getStaticProps()`
    
    이 함수는 pages 폴더 안에 있는 파일에서만 작동한다. 다른 폴더에 있는 파일에서는 불가능!
    
    이 함수는 이 페이지에서 필요한 데이터를 포함한 props를 준비한다. 또한 이 함수는 비동기적으로 설정될 수 있어서 유용함! `export async function getStaticProps()` → NextJS는 이 Promise가 반환될 때까지 기다린다.
    
    ```jsx
    // pages/index.js
    // getStaticProps() 함수에서 얻은 props를 여기서 받음
    function HomePage(props) {
      return <MeetupList meetups={props.meetups} />
    }   
    export async function getStaticProps() {
    	// 이 안에는 어떤 코드든지 실행 가능함
    	// ex. API or DB의 데이터 가져오는 로직 모두 가능
    	// 이 코드는 빌드 프로세스 중에 실행되는 함수이므로 클라이언트 측에서는 실행X
    	return {
    		props: {
    			meetups: DUMMY_MEETUPS
    		}, revalidate: 10 // 서버에 요청하는 간격 (초단위)
    	}; // 얻은 데이터를 반환해줘야함
     }
    export default HomePage;
    ```
    
2. 서버 사이드 렌더링
    
    정적 생성에서 revalidate 설정으로 해결되지 않는 동적인 반응을 해야하는 경우 혹은 데이터가 바로바로 바뀌는 경우에 사용
    
    ```jsx
    // pages/index.js
    // getServerSideProps() 함수에서 얻은 props를 여기서 받음
    function HomePage(props) {
      return <MeetupList meetups={props.meetups} />
    }   
    export async function getServerSideProps(context) {
    	const req = context.req // 요청
    	const res = context.res // 반응
    
    	// 이 안에는 어떤 코드든지 실행 가능함
    	// ex. API or DB의 데이터 가져오는 로직 모두 가능
    	// 이 코드는 빌드 프로세스 중에 실행되는 함수이므로 클라이언트 측에서는 실행X
    
    	return {
    		props: {
    			meetups: DUMMY_MEETUPS
    		}
    	}; // 얻은 데이터를 반환해줘야함
     }
    export default HomePage;
    ```
    
    - getStaticProps() 와의 차이점 : getServerSideProps()는 빌드 프로세스 중에는 실행X
    - getServerSideProps()의 단점 : 요청이 들어올 때까지 페이지가 만들어지는걸 기다림
    - 어떤 방법이 더 좋을까?
        - 요청객체에 접근할 필요가 없다면 정적 생성이 더 나음 ex.인증
        - 요청객체에 접근 해야하거나 초단위로 여러번 바뀌는 데이터를 가지고 있다면 revalidate가 도움이 안 되기 때문에 서버사이드 렌더링이 나음

    
getStaticPaths

만약 동적 페이지라면 getStaticProps을 이용한다

serversideprops를 사용하는게 아니라 사용하지 않는다면 getstaticprops를 이용해야 합니다

```jsx
export async function getStaticPaths() {
    // 채워넣기
}
```