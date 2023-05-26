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
import MorningView from '../components/MorningView.vue';
import LunchView from '../components/LunchView.vue';
import EveningView from '../components/EveningView.vue';
import DawnView from '../components/DawnView.vue';

export default {
  name: "movieList",
  components: {
    MovieListItem,
    MorningView,
    LunchView,
    EveningView,
    DawnView
  },
  data() {
    return {
      movie_list: [],
      currentView: '' // 현재 보여지는 뷰를 저장할 데이터
    };
  },
  methods: {
    logout() {
      this.$store.dispatch("Logout");
    },
  },
  computed: {
    lastLogin() {
      return this.$store.state.lastLogin;
    }
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
