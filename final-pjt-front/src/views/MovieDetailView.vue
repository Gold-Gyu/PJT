<template>
  <div class="article-page">
    <div>
      <h1>Movie Detail</h1>
      <movie-detail-item/>
      <MovieReview/>
    </div>

  </div>
</template>

<script>
import MovieDetailItem from "@/components/MovieDetailItem.vue";
import MovieReview from '../components/MovieReview.vue';
export default {
  name : "MovieDetail",
  components : {
    MovieDetailItem,
    MovieReview
  }
}
</script>

<style scoped>
.article-page {
  background: skyblue;
  min-height: 100vh;
  align-items: center;
  justify-content: center;
  padding: 30px;
  font-family: Arial, sans-serif;
}

</style>