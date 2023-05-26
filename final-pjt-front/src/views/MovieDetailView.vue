<template>
  <div class="article-page">
    <h1>Movie Detail</h1>
    <movie-detail-item/>
  </div>
</template>

<script>
import MovieDetailItem from "@/components/MovieDetailItem.vue";
// import MovieDetailItem from '../components/MovieDetailItem.vue';
export default {
  name : "MovieDetail",
  components : {
    MovieDetailItem
  }
}
</script>

<style>
/* .article-page {
  background: linear-gradient(to bottom, #C6426E, #642B73); */

/* } */
</style>