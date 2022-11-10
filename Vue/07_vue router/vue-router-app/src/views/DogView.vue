<template>
  <div>
    <!-- 이미지가 없다면 message를 표현 -->
    <p v-if="!imgSrc">{{ message }}</p>
    <img :src="imgSrc" alt="">
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'DogView',
  data() {
    return {
      imgSrc: null,
      message: '로딩 중',
    }
  },
  methods: {
    getDogImage() {
      const breed = this.$route.params.breed
      const dogImgUrl=`https://dog.ceo/api/breed/${breed}/images/random`
      
      axios({
        method: 'get',
        url: dogImgUrl,
      })
        .then((response) => {
          console.log(response)
          const imgSrc = response.data.message
          this.imgSrc = imgSrc
        })
        .catch((error) => {
          // this.message = `${this.$route.params.breed}는 없는 품종입니다`
          console.log(error)
          this.$router.push('/404')
        })
    }
  },
  created() {
    this.getDogImage()
  }
}
</script>

<style>

</style>