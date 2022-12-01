<template>
  <div class="about">
    <h1>This is an about page</h1>
    <router-link :to="{ name: 'home' }">홈으로! 선언형</router-link>
    <hr>
    <button @click="toHome">홈으로! 프로그래밍적인 방식</button>
    <hr>
    <input type="text" @keyup.enter="toHello" v-model="inputData"> 
  </div>
</template>
<script>
export default {
  name: 'AboutView',
  data() {
    return {
      inputData: '',
    }
  },
  methods: {
    toHome() {
      this.$router.push({ name: 'home' })
    },
    toHello() {
      this.$router.push({ name: 'hello', params: {userName: this.inputData} })
    }
  }
}
</script>
