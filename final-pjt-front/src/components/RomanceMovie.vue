<template>
    <div class="background">
      <h1 class="white">Romance</h1>
      <hr />
      <div class="card-container ">
        <b-card
          v-for="movie in movieList"
          :key="movie.id"
           
          :img-src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`"
          img-alt="Image"
          img-top
          class="movie-card cardBox"
          style="margin-bottom: 20px;"
          @click="goToDetail(movie)"
        >
          <b-card-text
          >
            <h5>{{ movie.title }}</h5>
            <p>평점: {{ movie.vote_average }}점</p>
            <p>개봉일: {{ movie.release_date }}</p>
          </b-card-text>
        </b-card>
      </div>
    </div>
  </template>
  
  <script>
  import 'animate.css';
  import axios from "axios";
  export default {
    name: "ActionMovie",
    data() {
      return {
        movieList: "",
      };
    },
    computed: {
      token() {
        return this.$store.state.token;
      },
    },
    created() {
      axios({
        method: "get",
        url: `http://127.0.0.1:8000/movies/genres/10749/`,

      })
        .then((res) => {
          this.movieList = res.data;
          console.log("action", res);
        })
        .catch((err) => {
          console.log("action's err", err);
        });
    },
    methods: {

        goToDetail(movie_list) {
          this.$router.push({
            name: "detail",
          });
          this.$store.dispatch("sendDetail", movie_list);
        },
    }
  };
  </script>
  
  <style>
  .background {
    background:  lightseagreen;
  }
  .white {
    color : white;
  }
  .cardBox {
    border: 3px solid lightcoral
  }
  .card-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
  }
  
  @media (max-width: 768px) {
    .card-container {
      justify-content: center;
    }
  }
  
  .movie-card {
    flex: 0 0 calc(20% - 20px);
    max-width: calc(20% - 20px);
    margin-bottom: 20px;
  }
  
  @media (max-width: 1200px) {
    .movie-card {
      flex: 0 0 calc(25% - 20px);
      max-width: calc(25% - 20px);
    }
  }
  
  @media (max-width: 992px) {
    .movie-card {
      flex: 0 0 calc(33.33% - 20px);
      max-width: calc(33.33% - 20px);
    }
  }
  
  @media (max-width: 768px) {
    .movie-card {
      flex: 0 0 calc(50% - 20px);
      max-width: calc(50% - 20px);
      border: 1rem solid light;
    }
  }
  </style>
  