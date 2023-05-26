<template>
  <div class="article-page">
    <h1 class="text">Profile</h1>

    <div class="d-flex justify-content-center align-items-center">
  <div>
    <b-container fluid>
      <b-row class="my-1">
        <b-col sm="5">
          <label><code class="text"> ID :</code></label>
        </b-col>
        <b-col sm="7">
          <b-form-input
            type="text"
            v-model="username"
          ></b-form-input>
        </b-col>
      </b-row>
    </b-container>
    <b-container fluid>
      <b-row class="my-1">
        <b-col sm="5">
          <label><code class="text"> Password :</code></label>
        </b-col>
        <b-col sm="7">
          <b-form-input
          type="password"
          v-model="password"
          ></b-form-input>
        </b-col>
      </b-row>
    </b-container>
    <b-container fluid>
      <b-row class="my-1">
        <b-col sm="5">
          <label><code class="text"> New Password :</code></label>
        </b-col>
        <b-col sm="7">
          <b-form-input
            type="password"
            v-model="new_password1"
          ></b-form-input>
        </b-col>
      </b-row>
    </b-container>
    <b-container fluid>
      <b-row class="my-1">
        <b-col sm="5">
          <label><code class="text"> New Password :</code></label>
        </b-col>
        <b-col sm="7">
          <b-form-input
            type="password"
            v-model="new_password2"
          ></b-form-input>
        </b-col>
      </b-row>
    </b-container>
    <button @click="changePassword" class="btn btn-primary">비밀번호 변경</button>
  </div>
</div>


    <!-- 비밀번호 변경 폼 -->
    <!-- <form @submit.prevent="changePassword">
      <label for="username">id:</label>
      <input type="text" id="username" v-model="username" />
      <label for="password">현재 비밀번호:</label>
      <input type="password" id="password" v-model="password" />
      <br />
      <label for="new-password1">새로운 비밀번호:</label>
      <input type="password" id="new-password1" v-model="new_password1" />
      <label for="new-password2">새로운 비밀번호확인:</label>
      <input type="password" id="new-password2" v-model="new_password2" />
      <br />
      <button type="submit">비밀번호 변경</button>
    </form> -->
  </div>
</template>

<script>
import axios from "axios";

// const token = this.$store.state.token
export default {
  data() {
    return {
      username: "",
      password: "",
      new_password1: "",
      new_password2: "",
    };
  },
  computed: {
    token() {
      return this.$store.state.token;
    },
  },

  methods: {
    changePassword() {
      const payload = {
        username: this.username,
        password: this.password,
        new_password1: this.new_password1,
        new_password2: this.new_password2,
        // Django에서 예상되는 CSRF 토큰 필드 이름인 'csrfmiddlewaretoken'을 사용하여 전달
      };
      axios({
        method: "post",
        url: `http://127.0.0.1:8000/auth/password/change/`,
        data: payload,
        headers: {
          Authorization: `Bearer ${this.token}`,
        },
      })
        // .put("http://127.0.0.1:8000/accounts/update_password/", )

        .then((response) => {
          alert("회원정보 변경이 완료되었습니다.")
          this.$router.push({ name : "home"})
          console.log(response.data);
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>

<style>
.btn-primary {
  padding: 10px 20px;
  font-size: 16px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.text {
  color: aliceblue;
}
.article-page {
  background: linear-gradient(to bottom, #C6426E, #642B73);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}
.justify-content-center {
  justify-content: center;
}
.align-items-center {
  align-content: center;
}

.text {
  color: white;
}

</style>
