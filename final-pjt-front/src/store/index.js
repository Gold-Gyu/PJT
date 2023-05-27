import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '../router'

const API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    articles : [],
    token: null,
    movie_list : [],
    movieDetail : [],
    articleDetail : [],
    userInfo: null,

  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    SAVE_USER(state, payload) {
      state.userInfo = payload.pk
    },
    LOGOUT(state) {
      state.token = null
      router.push({ name : "home"})
    },
    GET_ARTICLE(state, articles) {
      console.log(state)
      state.articles = articles
    },
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({name : 'home'})
    },
    SAVE_MOVIE(state, movie_list) {
      state.movie_list = movie_list
    },
    SAVE_MOVIE_DETAIL(state, payload) {
      
      const moviePk = payload.id
      const title = payload.title
      const overview = payload.overview
      const release_date = payload.release_date
      const vote_average = payload.vote_average
      const poster_path = payload.poster_path
      const popularity = payload.popularity
      const detailPackage = {moviePk, title,  overview, release_date, vote_average, poster_path, popularity}

      state.movieDetail = detailPackage

      
    },
    SAVE_ARTICLE_DETAIL(state, payload) {

      const id = payload.id
      const title = payload.title
      const content = payload.content
      const userid = payload.user_id
      const username = payload.user_username
      const detailArticle = {
        id, title, content, userid, username
      }
      state.articleDetail = detailArticle
    },

  },
  actions: {
    Logout(context) {
      console.log(context)
      context.commit("LOGOUT")
    },
    getArticles(context) {
      axios({
        method: 'get',
        url : "http://127.0.0.1:8000/articles/",
        headers : {
          Authorization : `Bearer ${context.state.token}`
        }
      })
      .then((res) => {
        context.commit('GET_ARTICLE', res.data)
      })
      .catch((err) =>{
        console.log(err)
      })
    },
    signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method : 'post',
        url : `${API_URL}/auth/signup/`,
        data: {
          username, password1, password2
        }
      })
      .then((res) => {
        // console.log(res.data)
        context.commit('SAVE_TOKEN', res.data.access)
      })
      .catch((err) => {
        alert("이미 존재하는 계정이거나 비밀번호가 일치하지 않습니다.")
        console.log(err)
      })
    },
    login(context, payload){
      const username = payload.username
      const password = payload.password
      axios({
        method : 'post',
        url : `${API_URL}/auth/login/`,
        data : {
          username, password
        }
      })
      .then((res) => {
        context.commit('SAVE_TOKEN', res.data.access)
        context.commit('SAVE_USER', res.data.user)
      })
      .catch((err) => {
        alert("로그인 정보가 틀리거나 ")
        console.log(err)
      })
    },
    sendDB(context, payload) {
        axios({
          method: 'post',
          url : `http://127.0.0.1:8000/movies/MovieCreate/`,
          data : {payload},
        })
        .then((res) => {
          console.log(res)
        })
        .catch((err) =>{
          
          console.log(err)
      })
    },
    SendToStore(context, payload) {
      const movie_list = payload
      this.commit("SAVE_MOVIE", movie_list)
    },
    sendDetail(context, payload){
      // console.log("this is store",payload)
      this.commit("SAVE_MOVIE_DETAIL", payload)
    },
    sendArticle(context, payload) {
      this.commit("SAVE_ARTICLE_DETAIL", payload)
    },

   
  },
  modules: {
  }
})