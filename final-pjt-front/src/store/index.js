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
    lastLogin: null,
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
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
      router.push({name : 'movieList'})
    },
    LOGIN_TO_MOVIELIST(state, token) {
      state.token = token
      router.push({name : 'movieList'})
    },
    SAVE_MOVIE(state, movie_list) {
      state.movie_list = movie_list
    },
    SAVE_MOVIE_DETAIL(state, payload) {
      console.log("바로 데이터를 저장한다.")
      const moviePk = payload.id
      const title = payload.title
      const overview = payload.overview
      const release_date = payload.release_date
      const vote_average = payload.vote_average
      const poster_path = payload.poster_path
      const popularity = payload.popularity
      const detailPackage = {moviePk, title,  overview, release_date, vote_average, poster_path, popularity}
      console.log("여기는 store의 detail", detailPackage)
      state.movieDetail = detailPackage
      console.log("store에 moviedetail", state.movieDetail)
      
    },
    SAVE_ARTICLE_DETAIL(state, payload) {

      const articlePk = payload.id
      const title = payload.title
      const content = payload.content
      const username = payload.user_username
      const detailArticle = {
        articlePk, title, content, username
      }
      state.articleDetail = detailArticle
    },
    UPDATE_LAST_LOGIN(state, lastLogin) {
      state.lastLogin = lastLogin
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
        // alert("다시 입력해주세요")
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
        console.log(res.data.access)
        const lastLogin = new Date()
        context.commit('UPDATE_LAST_LOGIN', lastLogin)
        context.commit('LOGIN_TO_MOVIELIST', res.data.access)
        console.log(lastLogin)
      })
      .catch((err) => {
        // alert("회원정보가 없습니다. 회원가입을 해주세요!")
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