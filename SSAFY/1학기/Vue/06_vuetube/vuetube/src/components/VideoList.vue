<template>
  <div>
    <ul class="list-group">
      <VideoListItem v-for="video in videos"
      :key="video.etag"
      :video="video"
      @selectThis="onSelect"
      />
    </ul>
  </div>
</template>

<script>
import VideoListItem from './VideoListItem.vue'

export default {
  name: 'VideoList',
  components: {
    VideoListItem,
  },
  props:{
    videos: Array,
  },
  methods:{
    onSelect(selectedVideo) {
      this.$emit('selectThis', selectedVideo)
    }
  }
}
</script>

<style>

</style>