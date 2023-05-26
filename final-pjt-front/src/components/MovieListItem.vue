<template>
  <div class="dawn-view">
    <carousel :navigation-enabled="true" :per-page-custom="[[320, 1], [480, 2], [720, 3], [960, 4]]" :autoplay="true" :autoplay-timeout="1000" :loop="true">
      <slide v-for="(movie, index) in movies_list" :key="movie.id" :style="slideStyle(index)">
        <img :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" :alt="movie.title"  @click="goToDetail(movie)"/>
        <div>{{ movie.title }}</div>
      </slide>
    </carousel>
  </div>
</template>

<script>
import { Carousel, Slide } from 'vue-carousel';

export default {
  components: {
    Carousel,
    Slide,
  },
  computed: {
    movies_list() {
      return this.$store.state.movie_list;
    },
  },
  methods: {
    goToDetail(movie_list) {
      
      this.$router.push({
        name: 'detail',
      })
      this.$store.dispatch("sendDetail", movie_list)
    },
    slideStyle(index) {
      if (index < this.movies_list.length - 1) {
        return { marginRight: '10px' };
      }
    }
  },
};
</script>

<style scoped>
.dawn-view {
  background-color: #221f1f; /* 넷플릭스 배경색 */
  padding: 30px;
  color: #fff;
  font-family: Arial, sans-serif;
}
/* 캐러셀 컨테이너 스타일 */
.carousel {
  display: flex;
  overflow-x: scroll;
  scroll-snap-type: x mandatory;
  scroll-behavior: smooth;
  -webkit-overflow-scrolling: touch;
}

/* 캐러셀 슬라이드 스타일 */
.slide {
  scroll-snap-align: start;
  flex: 0 0 auto;
  width: 80%;
  /* 슬라이드의 너비 조절 */
  margin-right: 1rem;
  /* 슬라이드 간 간격 설정 */
}

/* 캐러셀 이미지 스타일 */
.slide img {
  width: 100%;
  height: auto;
}

/* 캐러셀 타이틀 스타일 */
.slide div {
  text-align: center;
  font-weight: bold;
  margin-top: 0.5rem;
}

/* 캐러셀 네비게이션 버튼 스타일 */
.carousel-navigation button {
  background: none;
  border: none;
  cursor: pointer;
  font-size: 2rem;
  outline: none;
  padding: 0.5rem;
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
}

.carousel-navigation button.prev {
  left: 0;
}

.carousel-navigation button.next {
  right: 0;
}
</style>
