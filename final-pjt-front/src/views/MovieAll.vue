<template>
  <div class="back-page">
    <div>
      <b-card no-body class="boxList">
        <b-tabs card class="innerBox">
          <b-tab title="Action" active>
            <template v-slot:title>
              <button class="genreButton genreButton-action">Action</button>
            </template>
            <b-card-text>
              <ActionMovie></ActionMovie>
            </b-card-text>
          </b-tab>
          <b-tab title="Action" active>
            <template v-slot:title>
              <button class="genreButton genreButton-adventure">
                Adventure
              </button>
            </template>
            <b-card-text>
              <AdventureMovie></AdventureMovie>
            </b-card-text>
          </b-tab>
          <b-tab title="Action" active>
            <template v-slot:title>
              <button class="genreButton genreButton-fantasy">Fantasy</button>
            </template>
            <b-card-text>
              <FantasyMovie></FantasyMovie>
            </b-card-text>
          </b-tab>
          <b-tab title="Action" active>
            <template v-slot:title>
              <button class="genreButton genreButton-animation">
                Animation
              </button>
            </template>
            <b-card-text>
              <AnimationMovie></AnimationMovie>
            </b-card-text>
          </b-tab>
          <b-tab title="Action" active>
            <template v-slot:title>
              <button class="genreButton genreButton-horror">Horror</button>
            </template>
            <b-card-text>
              <HorrorMovie></HorrorMovie>
            </b-card-text>
          </b-tab>
          <b-tab title="Action" active>
            <template v-slot:title>
              <button class="genreButton genreButton-comedy">Comedy</button>
            </template>
            <b-card-text>
              <ComedyMovie></ComedyMovie>
            </b-card-text>
          </b-tab>
          <b-tab title="Action" active>
            <template v-slot:title>
              <button class="genreButton genreButton-thriller">Thriller</button>
            </template>
            <b-card-text>
              <ThrillerMovie></ThrillerMovie>
            </b-card-text>
          </b-tab>
          <b-tab title="Action" active>
            <template v-slot:title>
              <button class="genreButton genreButton-romance">Romance</button>
            </template>
            <b-card-text>
              <RomanceMovie></RomanceMovie>
            </b-card-text>
          </b-tab>
        </b-tabs>
      </b-card>
    </div>
  </div>
</template>

<script>
// import { Carousel, Slide } from "vue-carousel";
import ActionMovie from "@/components/ActionMovie.vue";
import AdventureMovie from "@/components/AdventureMovie.vue";
import FantasyMovie from "@/components/FantasyMovie.vue";
import AnimationMovie from "@/components/AnimationMovie.vue";
import HorrorMovie from "@/components/HorrorMovie.vue";
import ComedyMovie from "@/components/ComedyMovie.vue";
import ThrillerMovie from "@/components/ThrillerMovie.vue";
import RomanceMovie from "@/components/RomanceMovie.vue";
export default {
  components: {
    // Carousel,
    // Slide,
    ActionMovie,
    AdventureMovie,
    FantasyMovie,
    AnimationMovie,
    HorrorMovie,
    ComedyMovie,
    ThrillerMovie,
    RomanceMovie,
  },
  computed: {
    movies_list() {
      return this.$store.state.movie_list;
    },
  },
  methods: {
    getButton(title) {
      return `<button class="genreButton genreButton-action">${title}</button>`;
    },
    goToDetail(movie_list) {
      this.$router.push({
        name: "detail",
      });
      this.$store.dispatch("sendDetail", movie_list);
    },
    slideStyle(index) {
      if (index < this.movies_list.length - 1) {
        return { marginRight: "10px" };
      }
    },
  },
};
</script>

<style scoped>

.boxList{
  
}
.innerBox {
  background: lightseagreen;
}
.nobody {
  display: flex;
  justify-content: center;
}
.genreBox {
  display: flex;
  justify-content: center;
  /* align-items: center; */
  margin-bottom: 10px;
  
}
.genreButton {
  background: lightseagreen;
  margin: 5px;
  color: white;
  border-radius: 20px;
  border: none;
  padding: 10px 20px;
  font-size: 14px;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s;
}

.genreButton-action {
  background-color: #00aaff; /* 하늘색과 조화되는 배경색 */
}

.genreButton-adventure {
  background-color: #ffaa00; /* 다른 색상으로 변경 가능 */
}

.genreButton-fantasy {
  background-color: #55dd55; /* 다른 색상으로 변경 가능 */
}

.genreButton-animation {
  background-color: #ff55aa; /* 다른 색상으로 변경 가능 */
}

.genreButton-horror {
  background-color: #aa00aa; /* 다른 색상으로 변경 가능 */
}

.genreButton-comedy {
  background-color: #ffaa55; /* 다른 색상으로 변경 가능 */
}

.genreButton-thriller {
  background-color: #dd00dd; /* 다른 색상으로 변경 가능 */
}

.genreButton-romance {
  background-color: #aa55ff; /* 다른 색상으로 변경 가능 */
}

.genreButton:hover {
  opacity: 0.8;
}

.carousel {
  display: flex;
  overflow-x: scroll;
  scroll-snap-type: x mandatory;
  scroll-behavior: smooth;
  -webkit-overflow-scrolling: touch;
}

.slide {
  scroll-snap-align: start;
  flex: 0 0 auto;
  width: 80%;
  margin-right: 1rem;
}

.slide img {
  width: 100%;
  max-height: 200px;
  object-fit: cover;
}

.slide-title {
  text-align: center;
  font-weight: bold;
  margin-top: 0.5rem;
  width: 100%;
}

.back-page {
  background: skyblue;
  min-height: 100vh;
  align-items: center;
  justify-content: center;
  padding: 30px;
  font-family: Arial, sans-serif;
}
</style>
