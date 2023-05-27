<template>
    <div class="article-page">
      <div class="article-detail ">
  
      <h1>Comment</h1>
      <div class="comment-list">
        <div
          v-for="comment in commentList"
          :key="comment.id"
          class="comment-item"
        >
        <div class="d-flex justify-content-center ">
          
          <textarea class="comment-content" v-model="commentContent"></textarea>
          <p class="comment-user">작성자: {{ comment.user_username }}</p>
          <div v-if="comment.user_id == userId">
  
            <button class="submit-button left" @click="updateComment(comment.id)">
              UPDATE
            </button>
            <button class="delete-button" @click="deleteComment(comment.id)">
              DELETE
            </button>
          </div>
  
        </div>
        </div>
      </div>
      <hr />
  
    </div>
    </div>
    
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    name: "ArticleDetail",
    data() {
      return {
        commentContent: "",
        commentList: [],
        articleInfo : ''
      };
    },
    computed: {
      userId() {
        return this.$store.state.userInfo
      },
      article() {
        return this.$store.state.articleDetail;
      },
      token() {
        return this.$store.state.token;
      },
    },
    created() {
        this.showComment();
        console.log(this.$route.params.comment)
        this.commentContent = this.$route.params.comment.content
        this.articleInfo = this.$store.state.articleDetail
   
    },
    methods: {
      showComment() {
        axios({
          method: "get",
          url: `http://127.0.0.1:8000/articles/${this.article.id}/comment/create/`,
          headers: {
            Authorization: `Bearer ${this.token}`,
          },
        }).then((res) => {
          this.commentList = res.data;

        });
      },
      deleteComment(comment) {
        axios({
          method: "delete",
          url: `http://127.0.0.1:8000/articles/${this.article.id}/comment/delete/${comment}/`,
          headers: {
            Authorization: `Bearer ${this.token}`,
          },
        })
          .then(() => {
            this.showComment();
          })
          .catch((err) => {
            console.log(err);
          });
      },
      updateComment(comment) {
        axios({
        method: "PUT",
        url: `http://127.0.0.1:8000/articles/comment/delete/${comment}/`,
        data : {
            content : this.commentContent
        },
        headers: {
          Authorization: `Bearer ${this.token}`,
        },
      })
        .then(() => {
            this.$router.push({name : "articleDetail"})
          this.showComment();
        })
        .catch((err) => {
          console.log(err);
        });
      },
      deleteArticle(articleid){
        
        axios({
          method : "delete",
          url : `http://127.0.0.1:8000/articles/update/${articleid}/`,
          headers : {
            Authorization : `Bearer ${this.token}`
          }
        })
        .then((res) => {
          this.$router.push("article")
          console.log(res)
        })
        .catch((err) => {
          console.log(err)
        })
      },
      updateArticle(){
        const articleInfo = this.articleInfo
        this.$router.push({ name: "update", params:{article : articleInfo}})
      },
    },
  
  };
  </script>
  
  <style scoped>
  
  .left {
    margin-left: 8px;
  }
  .article-page {
    /* background: linear-gradient(to bottom, #C6426E, #642B73); */
    background: skyblue;
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  
  .mt {
    margin-bottom:  30px;
  }
  .blog-post {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    background-color: #fff;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    border-radius: 4px;
  }
  
  .blog-content {
    margin-bottom: 20px;
  }
  
  .blog-table {
    width: 100%;
    border-collapse: collapse;
  }
  
  .blog-table th {
    padding: 10px;
    text-align: left;
    background-color: #f2f2f2;
    font-weight: bold;
    border-bottom: 1px solid #ddd;
  }
  
  .blog-table td {
    padding: 10px;
    border-bottom: 1px solid #ddd;
  }
  
  .blog-table .author {
    color: #007bff;
  }
  
  @media screen and (max-width: 480px) {
    .blog-table th,
    .blog-table td {
      display: block;
      width: 100%;
    }
  
    .blog-table th {
      margin-top: 10px;
      font-size: 14px;
    }
  }
  .comment-input-field {
    width: 300px;
  }
  
  .article-detail {
    margin: 20px;
  }
  
  h1 {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 10px;
  }
  
  p {
    margin-bottom: 5px;
  }
  
  .comment-list {
    margin-bottom: 10px;
  }
  
  .comment-item {
    margin-bottom: 5px;
    padding: 10px;
    background-color: #f2f2f2;
    border-radius: 5px;
  }
  
  .comment-content {
    margin: 0;
  }
  .comment-details {
    display: flex;
    align-items: center;
  }
  .comment-user {
    margin: 0;
    font-size: 12px;
  }
  
  .delete-button {
    margin-left: 10px;
    font-size: 14px;
    padding: 5px 10px;
    background-color: #ff8080;
    color: white;
    border: none;
    border-radius: 5px;
  }
  
  .comment-input {
    margin-bottom: 10px;
  }
  
  .submit-button {
    font-size: 14px;
    padding: 5px 10px;
    background-color: #4caf50;
    color: white;
    border: none;
    border-radius: 5px;
  }
  
  .article-table {
    width: 100%;
    border-collapse: collapse;
  }
  
  .article-table th,
  .article-table td {
    padding: 8px;
    border: 1px solid #ccc;
  }
  
  .article-table th {
    text-align: left;
    background-color: #f2f2f2;
  }
  
  .article-table td {
    word-break: break-word;
  }
  
  .author {
    font-size: 12px;
    color: #888;
  }
  .center {
    text-align: center;
  }
  </style>
  