<template>
  <div>
    <div>
        <h1>{{userInfo.username}}님의 프로필</h1>
        <div>
            <h5>팔로우하기</h5>
            <h5>언팔로우하기</h5>
            <h5>팔로워</h5>
            <h5>팔로잉</h5>    
        </div>

        <div>
            <p>좋아요 한 영화</p>
            <p>{{ likeList }}</p>
        </div>
        
        <div>
            <p>작성한 게시글</p>
        </div>

        <div>
            <p>작성한 댓글</p>
        </div>
    </div>



  </div>

</template>

<script>
// import axios from "axios"
export default {
    name : "ProfileView",
    created() {

    },
    data() {
        return {
            username : ""
        }
    },
    computed : {
        userInfo() {
            return this.$store.state.userInfo
        },
        likeList() {
            return this.$store.state.likeList
        },
        token() {
            return this.$store.state.token
        }
    },
    methods : {

    }
}

</script>

<style>

</style>