<template>
  <div class='lunch'>
    <h1>점심메뉴</h1>
    <button @click="pickLunch">Pick Lunch</button>
    <p>{{ menu }}</p>
    <hr>
    <h2>로또를 뽑아보자</h2>
    <button @click="toLotto">Pick Lotto</button>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLunch',
  data() {
    return {
      lunchMenu: ['국밥', '치킨', '피자'],
      menu: null,
    }
  },
  methods: {
    pickLunch() {
      const menu = _.sample(this.lunchMenu)
      this.menu = menu
    },
    toLotto() {
      this.$router.push({ name: 'lotto'})
    }
  }
}
</script>

<style>

</style>