<template>
  <div class='lotto'>
    <h1>로또</h1>
    <button @click="lottoNumbers">Get Lucky Numbers</button>
    <p>{{ getNumbers }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLotto',
  data() {
    return {
      getNumbers: null,
    }
  },
  methods: {
    lottoNumbers() {
      this.getNumbers = _.sampleSize(_.range(1,46), 6)
      }
    }
  }
</script>

<style>

</style>