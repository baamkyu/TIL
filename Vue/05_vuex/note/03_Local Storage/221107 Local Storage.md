# 221107 Local Storage

# Local Storage

> Window.localStorage
> 
- 만료되지 않고 브라우저를 종료하고 다시 실행해도 데이터가 보존됨
- 관련 메서드
    - setItem(key, value) - key, value 형태로 데이터 저장
    - getItem(key) - key에 해당하는 데이터 조회

```jsx
// store/index.js

export default new Vuex.Store({
	...	
	actions: {
    createTodo(context, todoTitle) {
     ...
      context.dispatch('saveTodosToLocalStorage')
    },  
    deleteTodo(context, todoItem) {
      ...
      context.dispatch('saveTodosToLocalStorage')
    },
    updateTodoStatus(context, todoItem) {
      ...
      context.dispatch('saveTodosToLocalStorage')
    },
    saveTodosToLocalStorage(context) {
      const jsonTodos = JSON.stringify(context.state)
      localStorage.setItem('todos', jsonTodos)
    }
  },
```

```jsx
// store/index.js

export default new Vuex.Store({
	...
	getters:{
		...,
		LOAD_TODOS(state) {
      const localStorageTodos = localStorage.getItem('todos')
      const parsedTodos = JSON.parse(localStorageTodos)
      state.todos = parsedTodos
    }
	},
	...
	actions: {
			loadTodos(context) {
      context.commit('LOAD_TODOS')
    }
```

```jsx
// App.vue

<template>
	<div id="app">
		...
		<button @click=loadTodos">Todo 불러오기</button>
	</div>
</template>

<script>
export default {
	...,
	methods: {
    loadTodos() {
      this.$store.dispatch('loadTodos')
    }
	}
</script>
```

> vuex-presistedstated
> 

`npm i vuex-persistedstate` : 자동으로 저장되어있던 데이터를 불러와주는 패키지 install

```jsx
// store/index.js

import createPersistedState from 'vuex-persistedstate'

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
```

이걸 사용하면 전에 했던 loadTodos가 필요 없어짐.