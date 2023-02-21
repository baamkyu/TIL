# 221109 Vue Router

### UX & UI

> UX (User Experience)
> 
- 유저와 가장 가까이에 있는 분야, 데이터를 기반으로 유저를 조사하고 분석해서 개발자, 디자이너가 이해할 수 있게 소통
- 유저가 느끼는 느낌, 태도 그리고 행동을 디자인
    - 러쉬 매장 근처만 가도 맡을 수 있는 향기
    - 로딩이 너무 길어서 사용하고 싶지 않았던 사이트 등

- 좋은 UX를 설계하기 위해서는
    
    사람들의 마음과 생각을 이해하고 정리해서 녹여내는 과정이 필요
    
    유저 리서치, 데이터 설계 및 정제, 유저 시나리오, 프로토타입 설계 등이 필요
    

> UI (User Interface)
> 
- 유저에게 보여지는 화면을 디자인
- UX를 고려한 디자인을 반영, 이 과정에서 기능 개선 혹은 추가가 필요한 경우 front-end 개발자와 가장 많이 소통

- 좋은 UI를 설계하기 위해서는
    
    예쁜 디자인만 중요하다기보다는 사용자가 보다 쉽고 편리하게 사용할 수 있도록 하는 부분까지 고려해야 함
    
    통일된 디자인을 위한 디자인 시스템, 소통을 위한 중간 산출물, 프로토타입 등이 필요
    
    UI 디자인에 있어 가장 중요한 것은 “협업”
    

UX/UI 그리고 HCI

- GUI : 유저가 보는 일반적인 시각적인 디자인
- UI : 유저가 보거나 듣는 등 비시각적인 부분까지 포함한 디자인
- UX : 유저가 겪는 모든 경험 (컴퓨터와 관련 없는 것들까지 포함)
- HCI (Human Computer Interaction) : 인간과 컴퓨터 사이의 상호작용에 대한 학문

---

> Figma
> 
- 웹 기반 시스템을 가짐 → 매우 가벼운 환경에서 실행, 모든 작업 내역이 웹에 저장
- 실시간으로 팀원들이 협업할 수 있는 기능을 제공
- 직관적이고 다양한 디자인 툴을 제공
- 대부분의 기능을 무료로 사용할 수 있음

---

> Routing
> 
- 네트워크에서 경로를 선택하는 프로세스
- 웹 서비스에서의 라우팅
    - 유저가 방문한 URL에 대해 적절한 결과를 응답하는 것
    - ex. /articles/index/에 접근하면 articles의 index에 대한 결과를 보내줌

![Untitled](221109%20Vue%20Router%20d55d545cd3f44831a473e09187fa938f/Untitled.png)

> Vue Router
> 
- Vue의 공식 라우터
- 라우트에 컴포넌트를 매핑한 후, 어떤 URL에서 렌더링 할지 알려줌
    - 즉, SPA를 MPA처럼 URL을 이동하면서 사용 가능
    - SPA의 단점 중 하나인 “URL이 변경되지 않는다.”를 해결

---

## 실습

`vue create vue-router-app` : Vue 프로젝트 생성

`cd vue-router-app` : 폴더 이동

`vue add router` : Vue CLI를 통해 router plugin 적용 → 추가로 뜨는 거 모두 y

```html
	// App.vue

<template>
  <div id="app">
    <nav>
      <router-link to="/">Home</router-link> | 
      <router-link to="/about">About</router-link>
    </nav>
    <router-view/>
  </div>
</template>
```

`router-link` : 하나의 페이지처럼 보이는 곳으로 이동

```jsx
// src/router/index.js

const routes = [
	// /링크에 들어가면 home 보여주기
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
	// /about에 들어가면 about 보여주기
  {
    path: '/about',
    name: 'about',
]
```

라우터에 직접적인 영향을 끼치는 건 views에 작성, 영향 없는 하위 컴포넌트들은 component에 작성

> src/router/index.js
> 
- 라우터에 관련된 정보 및 설정이 작성되는 곳
- Django에서의 urls.py에 해당
- routes에 URL와 컴포넌트를 매핑

![Untitled](221109%20Vue%20Router%20d55d545cd3f44831a473e09187fa938f/Untitled%201.png)

> src/Views
> 
- router-view에 들어갈 component 작성
- 기존에 컴포넌트를 작성하던 곳은 components 폴더 뿐이었지만 이제 두 폴더로 나눠짐
- 각 폴더 안의 .vue 파일들이 기능적으로 다른 것은 아님
- views
    - routes에 매핑되는 컴포넌트
    - <router-view>의 위치에 렌더링 되는 컴포넌트를 모아두는 폴더
    - 다른 컴포넌트와 구분하기 위해 이름이 View로 끝나도록 만드는 것을 권장
    - ex. AboutView & HomeView 컴포넌트
- components
    - routes에 매핑된 컴포넌트의 하위 컴포넌트를 모아두는 폴더
    - ex. HomeView 컴포넌트 내부의 HelloWorld 컴포넌트

> 주소를 이동하는 2가지 방법
> 
1. 선언적 방식
2. 프로그래밍 방식

## 1. 선언적 방식

- router-link의 `to=""` 속성으로 주소 전달
    - 동적인 값을 사용하기 때문에 v-bind를 사용해야 정상적으로 작동
    - routes에 등록된 주소와 매핑된 컴포넌트로 이동
- 이름을 가지는 routes

```jsx
// App.vue
	<template>
  <div id="app">
    <nav>
      <router-link :to="{ name: 'home' }">Home</router-link> | 
      <router-link :to="{ name: 'about' }">About</router-link>
		</nav>
    <router-view/>
  </div>
</template>

// router/index.js
const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
```

## 2. 프로그래밍 방식

- Vue 인스턴스 내부에서 라우터 인스턴스에 `$router`로 접근할 수 있음
- 다른 URL로 이동하려면 `this.$router.push`를 사용
- 결국 `<router-link :to=”…”>`를 클릭하는 것과 `$router.push(...)`를 호출하는 것은 같은 동작

```jsx
// AboutView.vue
<template>
  <div class="about">
    <h1>This is an about page</h1>
    <router-link :to="{ name: 'home' }">홈으로! 선언형</router-link>
    <hr>
    <button @click="toHome">홈으로! 프로그래밍적인 방식</button>
  </div>
</template>
<script>
export default {
  name: 'AboutView',
  methods: {
    toHome() {
      this.$router.push({ name: 'home' })
    }
  }
}
</script>
```

> lazy-loading 방식
> 
- 모든 파일을 한 번에 로드하려고 하면 모든 걸 다 읽는 시간이 매우 오래 걸림
- 미리 로드를 하지 않고 특정 라우트에 방문할 때 로드하는 방식을 활용할 수 있음
    - 모든 파일을 한 번에 로드하지 않아도 되기 때문에 최초에 로드하는 시간이 빨라짐
    - 당장 사용하지 않을 컴포넌트는 먼저 로드하지 않는 것이 핵심
    
    ```jsx
    // src/router/index.js
    
    const routes = [
      {
        path: '/',
        name: 'home',
        component: HomeView
      },
    	{
        // component -> lazy-loading 방식 (첫 로딩에 렌더링 하지 않고, 해당 라우터가 동작할 때 컴포넌트를 렌더링 한다.)
        path: '/about',
        name: 'about',
        component: () => import('../views/AboutView.vue')
      },
    	...
    |
    ```
    

> 네비게이션 가드
> 
- Vue router를 통해 특정 URL에 접근할 때 다른 url로 redirect를 하거나 해당 URL로의 접근을 막는 방법
    - ex. 사용자의 인증 정보가 없으면 특정 페이지에 접근하지 못하게 함

> 네비게이션 가드의 종류
> 
- 전역 가드 : 애플리케이션 전역에서 동작
- 라우터 가드 : 특정 URL에서만 동작
- 컴포넌트 가드 : 라우터 컴포넌트 안에 정의

## 전역 가드 (Global Before Guard)

- 다른 url 주소로 이동할 때 항상 실행
- router/index.js에 `router.beforeEach()`를 사용하여 설정

```jsx
// src/router/index.js

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  console.log('to', to)
  console.log('from', from)
  console.log('next', next)
  next()
})

export default router
```

- 로그인 여부에 따른 라우팅 여부

```jsx
// App.vue
// LoginView에 대한 라우터 링크 추가
<template>
  <div id="app">
    <nav>
      ...
			<router-link :to="{name: 'login'}">Login</router-link>
    </nav>
    <router-view/>
  </div>
</template>
```

```jsx
// src/router/index.js
// hello 페이지로 가려고 하는데 로그인이 안 되어 있으면 login 페이지로 돌아가! 하는 코드

router.beforeEach((to, from, next) => {
  // 로그인 여부
  const isLoggedIn = false

  //로그인이 필요한 페이지
  const authPages = ['hello']

	// 이동할 페이지가 로그인이 필요한 사이트인지 확인
  const isAuthRequired = authPages.includes(to.name)

  if (isAuthRequired && !isLoggedIn) {
    next({name: 'login'})
  } else {
    next()
  }
})

export default router
```

## 라우터 가드

- 전체 route가 아닌 특정 route에 대해서만 가드를 설정하고 싶을 때 사용
- `beforeEnter()`
    - route에 진입했을 때 실행됨
    - 라우터를 등록한 위치에 추가
    - 단 매개변수, 쿼리, 해시 값이 변경될 때는 실행되지 않고 다른 경로에서 탐색할 때만 실행됨
    - 콜백 함수는 to, from, next를 인자로 받음

```jsx
// src/router/index.js
// 로그인 되어있는데 login창으로 가려고 하면 home으로 돌려 보냄

const isLoggedIn = true // 로그인이 되어있으면

const routes = [
	...,
	{
    path:'/login',
    name: 'login',
    component: LoginView,
    // 라우터가드 
    // 로그인 되어있는데 login으로 가려고 하면 home으로 돌려보냄
    beforeEnter(to, from, next) {
      if (isLoggedIn === true) {
        console.log('이미 로그인 되어있음!')
        next({ name: 'home' })
      } else {
        next()
      }
    },
  }
]
```

## 컴포넌트 가드

- 특정 컴포넌트 내에서 가드를 지정하고 싶을 때 사용
- `beforeRouteUpdate()` : 해당 컴포넌트를 렌더링하는 경로가 변경될 때 실행

```jsx
// src/views/HelloView.vue

<script>
export default {
  name: 'HelloView',
  data() {
    return {
      userName: this.$route.params.userName
    }
  },
  // 컴포넌트 가드 (입력값이 바뀌고 hello 누르면 이름이 ssafy로 바뀌어야하는데 안 따라감)
  // 파라미터가 변하는 것을 감지하게 도와줌 (경로가 바뀌면 이름도 바뀜)
  beforeRouteUpdate(to, from, next) {
    this.userName = to.params.userName
    next()
  }
}
</script>
```

---

# Articles 실습

`vue create articles`

`cd articles`

`vue add vuex`

`vue add router`

```jsx
// store/index.js
// 임의의 데이터 생성

export default new Vuex.Store({
  state: {
    article_id: 3,
    articles: [
      {
        id: 1,
        title: 'title',
        content: 'content',
        createdAt: new Date().getTime(),
      },
      {
        id: 2,
        title: 'title2',
        content: 'content2',
        createdAt: new Date().getTime(),
      }
    ]
  },
	...
})
```

```jsx
// index 구현
// views/IndexView.vue 생성

<template>
  <div>
    <h1>Articles</h1>
  </div>
</template>

<script>
export default {
  name: 'IndexView',
}
</script>

// router/index.js

import IndexView from '../views/IndexView.vue'

...
const routes = [
  {
    path: '/',
    name: 'index',
    component: IndexView
  },
	...
]
```

```jsx
// store/index.js의 state에서 불러온 articles 출력하기
// 어떤 형태로 불러올지 정하기 위해 components/ArticleItem.vue 생성

<template>
  <div>
    <p>글 번호 : {{ article.id }}</p>
    <p>글 제목 : {{ article.title }}</p>
  </div>
</template>

<script>
export default {
  name: 'ArticleItem',
  props: {
    article: Object,
  }
}

// views/IndexView.vue

<template>
  <div>
    <h1>Articles</h1>
    <ArticleItem 
    v-for="article in articles"
    :key="article.id"
    :article=article
    />
  </div>
</template>

<script>
import ArticleItem from '@/components/ArticleItem'

export default {
  name: 'IndexView',
  components: {
    ArticleItem,
  },
  computed: {
    articles() {
      return this.$store.state.articles
    }
  },
}
</script>
```

```jsx
// views/CreateView.vue 생성
<template>
  <div></div>
</template>

<script>
export default {
  name: 'CreateView',
}

// CreateView 생성한 것을 등록
// router/index.js

...
import CreateView from '../views/CreateView.vue'

...
const routes = [
  ...,
  {
    path: '/create',
    name: 'create',
    component: CreateView
  },
]
```

```jsx
// create 페이지 구성
// views/CreateView.vue
<template>
  <div>
    <h1>게시글 작성</h1>
    <form>
      <input type="text"><br>
      <textarea></textarea>
      <input type="submit">
    </form>
  </div>
</template>

// 입력한 데이터를 받아야 함
// .trim = 공백 제거 
<template>
  <div>
    <h1>게시글 작성</h1>
    <form>
      <input type="text" v-model.trim="title"><br>
      <textarea v-model.trim="content"></textarea>
      <input type="submit">
    </form>
  </div>
</template>

<script>
export default {
  name: 'CreateView',
  data() {
    return {
      title: null,
      content:null,
    }
  }
}
</script>

// 제출을 눌렀을 때 제출 막아주고 데이터를 변수에 입력받아서 보내야함
// views/CreateView.vue
<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle">
      ...
		</form>
	</div>
</template>

<script>
export default {
	...,
	methods: {
    createArticle() {
      const title = this.title
      const content = this.content
      const payload = {
        title, content
      }
      this.$store.dispatch('createArticle', payload)
    }
	}
}
</script>
```

```jsx
// 넘어온 데이터를 활용하여 article 생성 후 mutations 호출
// store/index.js
export default new Vuex.Store({
	...,
	actions: {
    createArticle(context, payload) {
      const article = {
        id: context.state.article_id,
        title: payload.title,
        content: payload.content,
        createAt: new Date().getTime()
      }
      context.commit('CREATE_ARTICLE', article)
    }
  },
	...
})

// mutations 호출
mutations: {
    CREATE_ARTICLE(state, article) {
      state.articles.push(article)
      state.article_id = state.article_id + 1
    }
```

```jsx
// 게시글 작성을 누르면 게시글 작성페이지로 이동하는 링크 추가
// views/IndexView.vue
<template>
  <div>
    <h1>Articles</h1>
    <router-link :to=" { name: 'create' } ">게시글 작성</router-link>
		...
	</div>
</template>

// 게시글 작성 페이지에서 뒤로 가기를 누르면 기본 페이지로 가는 링크 추가
<template>
	<div>
		...
		<router-link :to="{ name: 'index' }">뒤로가기</router-link>
  </div>
</template>

// 데이터 입력 하고 제출 눌렀을 때 index로 이동
<script>
export default {
	...
	methods: {
		...
		this.$router.push({ name: 'index' })
		}
	}
}
</script>

```