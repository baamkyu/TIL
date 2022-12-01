<template>
  <div id="app">
    <h1>버튼 박스 제작</h1>
    <h2>예약 페이지</h2>
    <h3>시간 선택</h3>
    <div class="d-flex flex-wrap">
      <div v-for="time in times" :key="time" class="px-3 mb-3" @click="clickBox(time)">
        <button class="noClick" :class="{'clicked' : timeLst.includes(time)}"> {{ time }} </button>
      </div>
    </div>
    <hr>
    <h3>선택 시간 : {{ timeLst }}</h3>
  </div>
</template>

<script>
export default {
  name: "App",
    data: function() {
    return {
      times: ["09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30",
              "14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30",
              "19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30"],
      timeLst: []
    }
  },
  methods: {
    clickBox: function(time){
      if (this.timeLst.includes(time)) {
        this.indexInData = this.timeLst.indexOf(time)
        this.timeLst.splice(this.indexInData)
      } else if (this.timeLst.length < 5) {
        this.timeLst.push(time)
      } else if (this.timeLst.length >= 5) {
        alert('다섯개까지만 선택 가능')
      } this.timeLst.sort()
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.noClick {
  background-color: white;
  color: black;
}

.clicked {
  background-color: gray;
  color: white;
}
</style>
