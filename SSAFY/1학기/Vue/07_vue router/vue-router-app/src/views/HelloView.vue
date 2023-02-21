<template>
  <div>
    <h1>
      hello, {{ userName }}
    </h1>
  </div>
</template>

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

<style>

</style>