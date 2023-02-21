# 221107 Todo with Vuex

> 개요
> 
- Vuex를 사용한 Todo 프로젝트 만들기
- 구현 기능
    - Todo CRUD
    - Todo  개수 계산
        - 전체 Todo
        - 완료된 Todo
        - 미완료된 Todo

![Untitled](221107%20Todo%20with%20Vuex%20d95ea45a029b4ceb8d8ef14e023c965c/Untitled.png)

![Untitled](221107%20Todo%20with%20Vuex%20d95ea45a029b4ceb8d8ef14e023c965c/Untitled%201.png)

> 실습
> 

프로젝트 생성 : `create vue todo-vuex-app`

폴더 이동 : `cd todo-vuex-app`

vuex 설치 : `vue add vuex` + y

파일 설정 : components 안에 TodoForm, TodoList, TodoListItem 생성

# READ

### 기본적인 파일 설정

1. TodoListItem.vue

```jsx
// components/TodoListItem.vue

<template>
  <div>TodoListItem</div>
</template>

<script>
export default {
  name: 'TodoListItem',
}
</script>
```

1. TodoList.vue

```jsx
// components/TodoList.vue
// 이름 설정 - 불러오기 - 사용

<template>
  <div>
		TodoList
    <TodoListItem/>
  </div>
</template>

<script>
import TodoListItem from '@/components/TodoListItem'

export default {
  name: 'TodoList',
  components: {
    TodoListItem,
  }
}
</script>
```

1. TodoForm.vue

```jsx
// components/TodoForm.vue

<template>
  <div>
    TodoForm
  </div>
</template>

<script>
export default {
  name: 'TodoForm',
}
</script>
```

1. App.vue

```
// App.vue
// 이름 설정 - 불러오기 - 사용하기

<template>
  <div id="app">
    <h1>Todo List</h1>
    <TodoList/>
    <TodoForm/>
  </div>
</template>

<script>
import TodoList from '@/components/TodoList'
import TodoForm from '@/components/TodoForm'

export default {
  name: 'App',
  components: {
    TodoList,
    TodoForm,
  }
}
</script>
```

### state 데이터 가져오기

```jsx
// components/TodoList.vue

<template>
  <div>
    <TodoListItem
      v-for="(todo, index) in todos"
      :key="index"
      :todo="todo"
    />
  </div>
</template>

<script>
	...
  computed: {
    todos() {
      return this.$store.state.todos
    }
  }
}
</script>
```

```jsx
// components/TodoListItem.vue

<template>
  <div>{{ todo.title }}</div>
</template>

<script>
export default {
  name: 'TodoListItem',
  props: {
    todo: Object,
  }
}
```

# CREATE

메서드(컴포넌트) —-dispatch ()—-> 액션 (todo) -—commit()---> 뮤테이션 (push) -> state

```jsx
// components/TodoList.vue
<template>
	...
</template>

<script>
import TodoListItem from '@/components/TodoListItem'

export default {
  name: 'TodoList',
  components: {
    TodoListItem,
  },
  computed: {
    todos() {
      return this.$store.state.todos
    }
  }
}
```

```jsx
// components/TodoForm.vue
<template>
	<div>
    <input 
    type="text"
    v-model.trim="todoTitle"  
    @keyup.enter="createTodo"
    >
    <!-- v-model.trim = 좌우 공백 제거 -->
  </div>
</template>

<script>
export default {
  name: 'TodoForm',
  data() {
    return {
      todoTitle: null,
    }
  },
  methods: {
    createTodo() {
      this.$store.dispatch('createTodo', this.todoTitle)
      this.todoTitle = null
    }
  }
}
</script>
```

```jsx
// store/index.js

export default new Vuex.Store({
  state: {
    todos: [],
  },
  getters: {
  },
  mutations: {
    CREATE_TODO(state, todoItem) {
      state.todos.push(todoItem)
    }
  },
  actions: {
		// 액션
    createTodo(context, todoTitle) {
      // Todo 객체 만들기
      const todoItem = {
        title: todoTitle,
        isCompleted: false,
      }
      context.commit('CREATE_TODO', todoItem)
    }
  },
  modules: {
  }
})
```

> 중간 정리
> 
- Vue ①컴포넌트의 method에서 dispatch()를 사용해 ②actions메서드를 호출
- Actions에 정의된 함수는 commit()을 사용해 ③mutations를 호출
- Mutations에 정의된 함수가 최종적으로 ④state를 변경

메서드(컴포넌트) --dispatch ()--> 액션 (todo) --commit()--> 뮤테이션 (push) -> state

# DELETE

```jsx
// components/TodoListItem.vue

// Delete 버튼 만들기
<template>
  <div>
    {{ todo.title }}
    <button @click="deleteTodo">Delete</button>
  </div>
</template>

// Delete 함수 만들기
<script>
export default {
  ...
  methods: {
    deleteTodo() {
      this.$store.dispatch('deleteTodo', this.todo)
    }
  }
}
</script>
```

```jsx
// store/index.js

// 액션, commit, state로 push
export default new Vuex.Store({
		...
    DELETE_TODO(state, todoItem) {
      const index = state.todos.indexOf(todoItem) // 몇번째 요소였는지 먼저 찾음
      state.todos.splice(index, 1) // 해당 인덱스부터 한개를 빼줌
    }
  },
  actions: {
    ...,
    deleteTodo(context, todoItem) {
      context.commit('DELETE_TODO', todoItem)
    }
  },
  modules: {
  }
})
```

# UPDATE

```jsx
// components/TodoListItem.vue

<script>
export default {
	...
	updateTodoStatus() {
      this.$store.dispatch('updateTodoStatus', this.todo)
    },
	}
}
</script>
```

```jsx
// store/index.js

export default new Vuex.Store({
	mutations: {
			...
			UPDATE_TODO_STATUS(state, todoItem) {
      // todos 배열에서 선택한 todo의 is_completed값만 토글한 후
      // 업데이트 된 todos 배열로 되어야 함
      state.todos = state.todos.map((todo) => {
        if (todo === todoItem) {
          todo.isCompleted = !todo.isCompleted
        }
        return todo
      })
		}
	},
	...
	actions: {
			updateTodoStatus(context, todoItem) {
      context.commit('UPDATE_TODO_STATUS', todoItem)
    }
	},
```

### style 입히기

title을 클릭하면 선이 그어지는 style 입히기

```jsx
// components/TodoListItem.vue

<template>
  <div>
    <span
      @click="updateTodoStatus"
      :class="{ 'is-completed': todo.isCompleted }"
    >
      {{ todo.title }}</span>
		<button @click="deleteTodo">Delete</button>
  </div>
</template>

<style>
  .is-completed {
    text-decoration: line-through;
  }
</style>
```

## getters

전체 Todo 개수 세기

```jsx
// store/index.js
export default new Vuex.Store({
		...
		getters: {
    allTodosCount(state) {
      return state.todos.length
    },
		...
})
```

```jsx
// App.vue
<template>
  <div id="app">
    ...
    <h2>모든 Todo 개수 : {{ allTodosCount }}</h2>
    ...
  </div>
</template>

<script>
export default {
	...
	computed: {
    allTodosCount() {
      return this.$store.getters.allTodosCount
    }
  }
}
</script>
```

### 완료된 Todo 개수

```jsx
// store/index.js

export default new Vuex.Store({
	getters: {
			...,
			completedTodosCount(state) {
      // 1. 완료된 부분만 모아놓은 새로운 배열을 생성
      const completedTodos = state.todos.filter((todo) => {
        return todo.isCompleted === true
      })
      // 2. 그 새로운 배열의 길이를 반환
      return completedTodos.length
    }
  },
```

```jsx
// App.vue

<template>
	<div id="app">
		...
		<h2>완료된 Todo 개수 : {{ completedTodosCount }}</h2>
		...
	</div>
</template>

<script>
export default {
	computed: {
    ...,
    completedTodosCount() {
      return this.$store.getters.completedTodosCount
    }
  }
}
</script>
```

### 미완료된 Todo 개수

(= 전체 Todo 개수 - 완료된 Todo 개수)

```jsx
// store.index.js

export default new Vuex.Store({
	getters: {
			...,
			unCompletedTodosCount(state, getters) {
      return getters.allTodosCount - getters.completedTodosCount
    },
  },
```

```jsx
// App.vue
<template>
  <div id="app">
    ...
    <h2>미완료된 Todo 개수 : {{ uncompletedTodosCount}}</h2>
    ...
  </div>
</template>

<script>
export default {
	...
	computed: {
			uncompletedTodosCount() {
      return this.$store.getters.uncompletedTodosCount
    }
  }
}
</script>
```