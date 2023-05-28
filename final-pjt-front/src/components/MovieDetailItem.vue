<template>
  <div class="box">


    <div class="container">
      <div class="image-section">
        <b-card class="imgsize" :img-src="`https://image.tmdb.org/t/p/w500/${movieDetailList.poster_path}`"></b-card>
      </div>
      <div class="info-section">
        <div class="movie-info">
          <div class="info-row">
            <p class="info-label">제목:</p>
            <p class="info-value">{{ movieDetailList.title }}</p>
          </div>
          <div class="info-row">
            <p class="info-label">줄거리</p>
            <p class="info-value ">{{ movieDetailList.overview }}</p>
          </div>
          <div class="info-row">
            <p class="info-label">개봉일:</p>
            <p class="info-value">{{ movieDetailList.release_date }}</p>
          </div>
          <div class="info-row">
            <p class="info-label">관객수:</p>
            <p class="info-value">{{ movieDetailList.popularity }}</p>
          </div>
          <div class="info-row">
            <p class="info-label">평점:</p>
            <p class="info-value">{{ movieDetailList.vote_average }}</p>
          </div>
        </div>
        <div class="review-section">
          <div class="input-wrapper">
            <input type="text" v-model="reviewContent" placeholder="리뷰 작성" class="input-field" />
          </div>
          <button @click="sendToMovie" class="submit-button">등록</button>
        </div>
        <div class="rating-section margin-bottom">
          <span>별점:</span>
          <template >
            <span
              v-for="i in 5"
              :key="i"
              :class="{ active: i <= rank }"
              @click="rank = i"
            >★</span>
          </template>
        </div>
      </div>
    </div>
    <div>
      <br>
      <br>
      <h1>REVIEWS</h1>
      <hr>
      <div class="reviewBox">

        <ul class="review-list">
          <li v-for="(review, index) in reviews" :key="index" class="review-item">
            <div class="review-rating">
              <span v-for="n in 5" :key="n" class="star" :class="{ filled: n <= review.rank, empty: n > review.rank }">★</span>
            </div>
            <div class="review-content">{{ review.content }}</div>
            <p class="username">{{ review.username }}</p>
            <button @click="deleteReview(review)" class="delete-button">삭제</button> 
          </li>
        </ul>

      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "MovieDetailItem",
  data() {
    return {
      moviePk: null,
      reviewContent: "",
      rank: 0,
      reviews: null,
    };
  },
  computed: {
    movieDetailList() {
      return this.$store.state.movieDetail;
    },
    token() {
      return this.$store.state.token;
    },
  },
  methods: {
    deleteReview(review){
      axios({
        method : "delete",
        url : `http://127.0.0.1:8000/movies/reviewDelete/${review.id}/`,
        headers : {
          Authorization : `Bearer ${this.token}`
        }
      })
      .then(() => {
        axios({
          method: "GET",
          url: `http://127.0.0.1:8000/movies/reviews/${this.movieDetailList.moviePk}/`,
        })
        .then((res) => {
          this.reviews = res.data;
        })
        .catch((err) => {
          console.log(err)
        })
      })
      .catch((err) => {
        console.log(err)
      })
    },
    sendToMovie() {
      if (!this.reviewContent || this.rank === 0) {
        alert("리뷰 내용과 별점을 입력해주세요.");
        return;
      }

      axios({
        method: "POST",
        url: `http://127.0.0.1:8000/movies/MovieDetail/${this.movieDetailList.moviePk}/reviews/`,
        data: {
          content: this.reviewContent,
          rank: this.rank,
        },
        headers: {
          Authorization: `Bearer ${this.token}`,
        },
      })
        .then(() => {
          console.log(this.rank);
          this.reviewContent = "";
          this.rank = 0;
          this.createReview();
        })
        .catch(() => {
          console.log(this.token);
        });
    },
    createReview() {
      axios({
        method: "GET",
        url: `http://127.0.0.1:8000/movies/reviews/${this.movieDetailList.moviePk}/`,
      })
      .then((res) => {
        this.reviews = res.data;
        console.log(res.data);
      })
      .catch((err) => { 
        console.log(err)
      })
    },
  },
  created() {
    axios({
      method: "GET",
      url: `http://127.0.0.1:8000/movies/reviews/${this.movieDetailList.moviePk}/`,
    })
      .then((res) => {
        this.reviews = res.data;
      });
  },
};
</script>

<style scoped>

.reviewBox {
  display: flex;
  justify-content: center;
}
.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f5f5f5;
  border-radius: 10px;
  display: flex;

}

.image-section {
  flex: 1;
  margin-right: 20px;
}

.info-section {
  flex: 2;
}

.imgsize {
  width: 100%;
  height: auto;
  border-radius: 10px;
}

.movie-info {
  margin-bottom: 20px;
}

.info-row {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.info-label {
  font-weight: bold;
  margin-right: 10px;
}

.review-section {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.input-wrapper {
  flex: 1;
  margin-right: 10px;
}

.input-field {
  width: 100%;
  padding: 8px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.submit-button {
  background-color: #4caf50;
  color: white;
  border: none;
  padding: 8px 12px;
  font-size: 14px;
  border-radius: 4px;
  cursor: pointer;
}

.submit-button:hover {
  background-color: #45a049;
}

.submit-button:focus {
  outline: none;
}

.rating-section {
  display: flex;
  align-items: center;
}

.rating-section span {
  cursor: pointer;
  font-size: 20px;
  margin-right: 5px;
}

.rating-section span.active {
  color: rgb(241, 241, 53);
}

.review-list {
  list-style-type: none;
  padding: 0;
}

.review-item {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.review-content {
  font-weight: bold;
  margin-left: 5px;
}

.review-rating {
  display: flex;
  justify-content: flex-end;
  align-items: center;
  margin-right: 5px;
}

.star {
  color: rgb(241, 241, 53);
  margin-left: 3px;
}

.star.filled {
  color: rgb(241, 241, 53);
}

.star.empty {
  color: #000;
}

.username {
  margin-left: 10px;
  font-size: 14px;
  color: #888;
  margin-right: 10px;
}

.delete-button {
  background-color: #f44336;
  color: white;
  border: none;
  padding: 6px 12px;
  font-size: 14px;
  border-radius: 4px;
  cursor: pointer;
}

.delete-button:hover {
  background-color: #d32f2f;
}

.delete-button:focus {
  outline: none;
}


</style>
