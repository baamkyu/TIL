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

<style>

</style>