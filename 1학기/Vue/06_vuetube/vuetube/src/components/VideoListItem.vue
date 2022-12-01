<template>
  <div>
    <li class="list-group-item video-item" @click="pickOne">
      <img :src="videoImgUrl" alt="not thumbnail">
      <div>{{ video.snippet.title }}</div>
    </li>
  </div>
</template>

<script>
export default {
  name: 'VideoListItem',
  props:{
    video: Object,
  },
  methods:{
    pickOne () {
      this.$emit('selectThis', this.video)
    }
  },
  computed: {
    videoImgUrl() {
      return this.video.snippet.thumbnails.default.url
    },
  }
}
</script>

<style>
  .video-item {
    display: flex;
    cursor: pointer;
  }

  .video-item:hover {
    background-color: lightgray;
  }
</style>