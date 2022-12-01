<template>
  <div id="app" class="container vuetube-wrap">
    <!-- 제목 영역 -->
    <header class="d-flex justify-content-center">
      <h1 class="mt-4 text-primary">SSAFY TUBE</h1>
    </header>

    <!-- 검색바 -->
    <SearchBar @fetch-videos="onFetchVideos"/>

    <!-- 본문 영역 (비디오와 비디오리스트) -->
    <section class="row mt-4">
      <!-- 비디오 플레이 영역 -->
      <div class="col-12 col-lg-8">
        <VideoDetail v-if="isSelectedVideo" :selectedVideo="selectedVideo"/>
        <div v-else class="unselected">
          <div class="img-area">
            <div>
              <img src="./assets/noResult.png" alt="noResult">
            </div>
            <p class="mt-4">선택된 비디오가 없습니다!</p>
            <p>비디오를 검색하거나 리스트에서 골라주세요!</p>
          </div>
        </div>
      </div>
      <!-- 오른쪽에 보일 비디오 리스트 5개 -->
      <aside class="col-12 col-lg-4">
        <VideoList :videos="videos"
        @selectThis="onSelect"
        />
      </aside>
    </section>

  </div>
</template>

<script>
import SearchBar from './components/SearchBar.vue'
import VideoDetail from './components/VideoDetail.vue'
import VideoList from './components/VideoList.vue'

export default {
  name: 'App',
  components: {
    SearchBar,
    VideoDetail,
    VideoList,
  },
  data() {
    return {
      videos: [],
      selectedVideo: {},
    }
  },
  methods: {
    onFetchVideos(videos) {
      this.videos = videos
    },
    onSelect(selectedVideo) {
      this.selectedVideo = selectedVideo
    }
  },
  computed: {
    isSelectedVideo() {
      return !!Object.keys(this.selectedVideo).length
    }
  }
}
</script>

<style>
  .vuetube-wrap {
    /* 최소 높이는 100 viewport height */
    min-height: 100vh;
  }
</style>
