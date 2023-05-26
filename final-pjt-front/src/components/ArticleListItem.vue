<template>
  <div class="bulletin-board">
    <div v-for="article in articles" :key="article.id" class="article-card" @click="goDetail(article)">
      <h1 class="article-title">{{ article.title }}</h1>
      <p class="article-author">작성자: {{ article.user_username }}</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ArticleListItem",
  data() {
    return {
      articles: null,
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
      url: "http://127.0.0.1:8000/articles/",
      data: {},
      headers: {
        Authorization: `Bearer ${this.token}`,
      },
    })
      .then((res) => {
        this.articles = res.data;
        console.log(this.articles);
      })
      .catch((err) => {
        console.log(err);
      });
  },
  methods: {
    goDetail(article) {
      console.log(article);
      console.log("클릭 발생");
      this.$router.push({
        name: "articleDetail",
        params: { article: article },
      });
      this.$store.dispatch("sendArticle", article);
    },
  },
};
</script>

<style scoped>
.bulletin-board {
  margin: 20px;
}

.article-card {
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 10px;
  margin-bottom: 10px;
  cursor: pointer;
}

.article-title {
  font-size: 20px;
  font-weight: bold;
  margin-bottom: 5px;
}

.article-author {
  font-size: 16px;
  color: #555;
}

hr {
  border: none;
  border-top: 1px solid #ccc;
  margin: 5px 0;
}
</style>
