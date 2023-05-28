<template>
  <div class="article-page">
    <div class="container">
      <h1>Article Page</h1>
      <div class="create-container">
        <button @click="redirectToCreate" class="create-button">CREATE</button>
      </div>
      <div class="form-container">
        <form>
          <div class="form-group">
            <label for="title">게시글 제목 : </label>
            <div class="input-group">
              <input type="text" id="title" v-model="searchTitle" class="form-control" placeholder="제목을 입력하세요">
              <button type="submit" class="btn btn-primary">검색</button>
            </div>
          </div>
        </form>
      </div>
      <article-list :articles="filteredArticles"></article-list>
    </div>
  </div>
</template>

<script>
import ArticleList from "@/components/ArticleList.vue";

export default {
  name: 'ArticleListView',
  components: {
    ArticleList
  },
  data() {
    return {
      searchTitle: '',
      searchAuthor: '',
      articleInfo: '',
    };
  },
  computed: {
    filteredArticles() {
      let filtered = this.articles;
      if (this.searchTitle) {
        filtered = filtered.filter(article => article.title.toLowerCase().includes(this.searchTitle.toLowerCase()));
      }
      if (this.searchAuthor) {
        filtered = filtered.filter(article => article.author === this.searchAuthor);
      }
      return filtered;
    }
  },
  methods: {
    redirectToCreate() {
      // 네비게이션 가드 등의 로직을 추가하여 CREATE 페이지로 이동하도록 구현해야 합니다.
      // 예시로 라우터를 사용하여 페이지 이동하는 방식을 보여드리겠습니다.
      this.$router.push("/create");
    }
  },
  created() {
    // this.articleInfo = this.$route.params.article
    // console.log(this.articleInfo)
  }
};
</script>

<style scoped>
.container {
  background-color: #ffffff;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

h1 {
  text-align: center;
  margin-bottom: 20px;
  color: #333;
  font-size: 24px;
}

.create-container {
  text-align: center;
  margin-bottom: 10px;
}

.create-button {
  padding: 8px 16px;
  font-size: 16px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.create-button:hover {
  background-color: #0056b3;
}

.form-container {
  margin-bottom: 20px;
}

.form-group {
  margin-bottom: 10px;
}

.form-control {
  padding: 8px;
  border-radius: 4px;
  border: 1px solid #ccc;
}

.btn-primary {
  padding: 8px 10px;
  margin-left: 5px;
  font-size: 16px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.btn-primary:hover {
  background-color: #0056b3;
}

.article-list {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-gap: 20px;
  margin-top: 20px;
}

.card {
  background-color: #fff;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.card-header {
  margin-bottom: 10px;
}

.card-title {
  font-size: 18px;
  font-weight: bold;
}

.card-author {
  font-size: 14px;
  color: #555;
  margin-bottom: 5px;
}

.card-content {
  font-size: 14px;
  color: #777;
}

.article-page {
  background: skyblue;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
