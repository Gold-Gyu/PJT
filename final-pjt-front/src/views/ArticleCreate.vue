<template>
  <div class="time-travel-bg article-page">
    <b-container>
      <h1>게시물 작성</h1>
      <b-row class="my-4">
        <b-col sm="2" class="text-right">
          <label for="input-default" class="title-label">제목</label>
        </b-col>
        <b-col sm="10">
          <b-form-input id="input-default" placeholder="제목을 작성하세요." v-model="title" class="title-input"></b-form-input>
        </b-col>
      </b-row>

      <b-row class="mt-4">
        <b-col sm="2" class="text-right">
          <label for="textarea-default" class="content-label">내용</label>
        </b-col>
        <b-col sm="10">
          <b-form-textarea id="textarea-default" placeholder="내용을 입력하세요." v-model="content" rows="8" class="content-input"></b-form-textarea>
        </b-col>
      </b-row>

      <b-row class="mt-4">
        <b-col sm="12" class="text-center">
          <b-button variant="primary" @click="create_article">작성하기</b-button>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>
<script>
import axios from 'axios'
// const API_URL = 'http://127.0.0.1:8000'

export default {
    name : "CreateView",
    computed : {
        isLogin() {
            return this.$store.getters.isLogin
        }
    },
    created() {
        this.getArticles()
    },
    data() {
        return {
            title : "",
            content : ""
        }
    },
    methods : {
      getArticles() {

            

    },
    create_article() {
        const title = this.title
        const content = this.content
        if (this.isLogin) {
            this.$store.dispatch('getArticles')
        }

        else {
            alert('로그인이 필요한 페이지')
            this.$router.push({ name : 'login'})
        }
        if (!title) {
            alert('제목 입력해주세요')
            return
        } else if (!content){
            alert('내용 입력해주세요')
            return
        }
        axios({
            method: 'post',
            url : 'http://127.0.0.1:8000/articles/',
            data : { 
              title : title, 
              content : content },
            headers : {
                Authorization : `Bearer ${this.$store.state.token}` 
            }
            })
            .then((res) => {
              console.log(res)
                this.$router.push({name : 'article'})
            })
            .catch((err) => {
                console.log(err)
            })
            
    }
}
}
</script>


<style scoped>

.article-page {
  background: skyblue;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.time-travel-bg {
  /* background-image: url('https://images.unsplash.com/photo-1574267432553-4b4628081c31?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1931&q=80'); */
  /* background-image: url('https://plus.unsplash.com/premium_photo-1680265343643-6994bdb74dd7?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1074&q=80'); */
  background-size: cover;
  background-position: center;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.title-label {
  font-weight: bold;
  font-size: 20px;
  color: #333;
  margin-bottom: 10px;
}

.title-input {
  font-size: 20px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.content-label {
  font-weight: bold;
  font-size: 18px;
  color: #333;
  margin-bottom: 10px;
}

.content-input {
  font-size: 16px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  resize: vertical;
}

.b-button {
  padding: 10px 20px;
  font-size: 18px;
}
</style>