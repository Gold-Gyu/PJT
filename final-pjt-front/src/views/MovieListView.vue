<template>
  <div>
    <component :is="currentView"></component>
    <!-- <MovieListItem/> -->


    
  </div>
</template>

<script>
import 'animate.css';
import axios from "axios";
import MovieListItem from '../components/MovieListItem.vue';

export default {
  name: "movieList",
  components: {
    MovieListItem,
  },
  data() {
    return {
      movie_list: [],
    };
  },
  methods: {

  },
  computed: {

  },
  created() {
    axios({
      method: "get",
      url: "http://127.0.0.1:8000/movies/ServerToClient/",
    })
    .then((res) => {
      console.log(res);
      this.$store.dispatch("SendToStore", res.data);

      // 현재 시간을 기준으로 해당하는 뷰를 선택
      const currentTime = new Date();
      const currentHour = currentTime.getHours();

      if (currentHour >= 6 && currentHour < 12) {
        this.currentView = "MorningView";
      } else if (currentHour >= 12 && currentHour < 18) {
        this.currentView = "LunchView";
      } else if (currentHour >= 18 && currentHour < 24) {
        this.currentView = "EveningView";
      } else {
        this.currentView = "DawnView";
      }
    });
  },
};
</script>

<style></style>
