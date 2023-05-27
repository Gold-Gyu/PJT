<template>
  <div>
    <div id="back">
      <canvas id="canvas" class="canvas-back"></canvas>
      <div class="backRight"></div>
      <div class="backLeft"></div>
    </div>

    <div id="slideBox">
      <div class="topLayer">
        <div class="left">
          <div class="content">
            <h2>Sign Up</h2>
            <form id="form-signup" method="post" @submit.prevent="submitSignUp">
              
              <div class="form-element form-stack ">
                <label for="username-signup" class="form-label">Username</label>
                <input id="username-signup" type="text" name="username" v-model="signup.username" />
              </div>
              <div class="form-element form-stack">
                <label for="password-signup" class="form-label">Password</label>
                <input id="password-signup" type="password" name="password" v-model="signup.password" />
              </div>
              <div class="form-element form-stack">
                <label for="password-signup" class="form-label">Password Confirm</label>
                <input id="password-signup" type="password" name="password" v-model="signup.password2" />
              </div>
            
              <div class="form-element form-submit">
                <button id="signUp" class="signup" type="submit" name="signup" >
                  Sign up
                </button>
                <button id="goLeft" class="signup off" @click="goLeft" @click.prevent="goLeft">Log In</button>
              </div>
            </form>
          </div>
        </div>
        <div class="right">
          <div class="content">
            <h2>Login</h2>
            
            <form id="form-login" method="post" @submit.prevent="submitLogin">
              <div class="form-element form-stack">
                <label for="username-login" class="form-label">Username</label>
                <input id="username-login" type="text" name="username" v-model="login.username" />
              </div>
              <div class="form-element form-stack">
                <label for="password-login" class="form-label">Password</label>
                <input id="password-login" type="password" name="password" v-model="login.password" />
              </div>
              <div class="form-element form-submit flex">
                <button id="logIn" class="login" type="submit" name="login" @submit.prevent="submitLogin">
                  Log In
                </button>
                <button id="goRight" class="login off" @click="goRight" @click.prevent="goRight">Sign Up</button>
              </div>

                

            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import $ from "jquery";
import { paper, Point, Path, Group } from "paper";

export default {
  data() {
    return {
      signup: {
    
        username: '',
        password: '',
        password2: '',
        confirm: false
      },
      login: {
        username: '',
        password: ''
      }
    };
  },
  mounted() {
    this.setupPaper();
  },
  methods: {
    submitSignUp() {
      // Sign up form submit 처리
      
      const username = this.signup.username
      const password1 = this.signup.password
      const password2 = this.signup.password2


      const payload = {
        username, password1, password2
      }

      this.$store.dispatch('signUp', payload)
    },
    submitLogin() {
      // Login form submit 처리
      const username = this.login.username
      const password = this.login.password

      const payload = {
        username, password
      }
      this.$store.dispatch('login', payload)
    },
    goRight() {
      $("#slideBox").animate({
        marginLeft: "0",
      });
      $(".topLayer").animate({
        marginLeft: "100%",
      });
    },
    goLeft() {
      if (window.innerWidth > 769) {
        $("#slideBox").animate({
          marginLeft: "50%",
        });
      } else {
        $("#slideBox").animate({
          marginLeft: "75%",
        });
      }
      $(".topLayer").animate({
        marginLeft: "0",
      });
    },
    setupPaper() {
      paper.setup("canvas");
      const path = new Path.Rectangle({
        point: [75, 75],
        size: [75, 75],
        strokeColor: "black",
      });
      const group = new Group([path]);
      group.applyMatrix = false;
      group.scaling = new Point(0.01, 0.01);
      group.onFrame = function (event) {
        console.log(event)
        this.rotate(1);
        this.scaling += new Point(0.005, 0.005);
        if (this.scaling.x > 1.5) {
          this.scaling = new Point(0.01, 0.01);
        }
      };
      paper.view.draw();
    },
  },
};
</script>

<style lang="scss">

.checkbox {
    /* 원하는 크기로 조정하세요 */
    width: 20px;
    height: 20px;
  }
$theme-signup: #03A9F4;
$theme-signup-darken: #0288D1;
$theme-signup-background: #2C3034;
$theme-login: #673AB7;
$theme-login-darken: #512DA8;
$theme-login-background: #f9f9f9;
$theme-dark: #212121;
$theme-light: #e3e3e3;
$font-default: 'Roboto', sans-serif;

$success: #5cb85c;
$error: #d9534f;

body {
  margin: 0;
  height: 100%;
  overflow: hidden;
  width: 100% !important;
  box-sizing: border-box;
  font-family: $font-default;
}

.backRight {
  position: absolute;
  right: 0;
  width: 50%;
  height: 100%;
  background: $theme-signup;
}

.backLeft {
  position: absolute;
  left: 0;
  width: 50%;
  height: 100%;
  background: $theme-login;
}

#back {
  width: 100%;
  height: 100%;
  position: absolute;
  z-index: -999;
}

.canvas-back {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 10;
}

#slideBox {
  width: 50%;
  max-height: 100%;
  height: 100%;
  overflow: hidden;
  margin-left: 50%;
  position: absolute;
  box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22);
}

.topLayer {
  width: 200%;
  height: 100%;
  position: relative;
  left: 0;
  left: -100%;
}

label {
  font-size: 0.8em;
  text-transform: uppercase;
}

input {
  background-color: transparent;
  border: 0;
  outline: 0;
  font-size: 1em;
  padding: 8px 1px;
  margin-top: 0.1em;
}

.left {
  width: 50%;
  height: 100%;
  overflow: scroll;
  background: $theme-signup-background;
  left: 0;
  position: absolute;
  label {
    color: $theme-light;
  }
  input {
    border-bottom: 1px solid $theme-light;
    color: $theme-light;
    &:focus, &:active {
      border-color: $theme-signup;
      color: $theme-signup;
    }
    &:-webkit-autofill {
      -webkit-box-shadow: 0 0 0 30px $theme-signup-background inset;
      -webkit-text-fill-color: $theme-light;
    }
  }
  a {
    color: $theme-signup;
  }
}

.right {
  width: 50%;
  height: 100%;
  overflow: scroll;
  background: $theme-login-background;
  right: 0;
  position: absolute;
  label {
    color: $theme-dark;
  }
  input {
    border-bottom: 1px solid $theme-dark;
    &:focus, &:active {
      border-color: $theme-login;
    }
    &:-webkit-autofill {
      -webkit-box-shadow: 0 0 0 30px $theme-login-background inset;
      -webkit-text-fill-color: $theme-dark;
    }
  }
}

.content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  min-height: 100%;
  width: 80%;
  margin: 0 auto;
  position: relative;
}

.content h2 {
  font-weight: 300;
  font-size: 2.6em;
  margin: 0.2em 0 0.1em;
}

.left .content h2 {
  color: $theme-signup;
}

.right .content h2 {
  color: $theme-login;
}

.form-element {
  margin: 1.6em 0;
  &.form-submit {
    margin: 1.6em 0 0;
  }
}

.form-stack {
  display: flex;
  flex-direction: column;
}

.form-checkbox {
  display: flex;
  align-items: center;
  
  label {
    margin: 0 6px 0;
    font-size: 0.72em;
  }
}

button {
  padding: 0.8em 1.2em;
  margin: 0 10px 0 0;
  width: auto;
  font-weight: 600;
  text-transform:  uppercase;
  font-size: 1em;
  color: #fff;
  line-height: 1em;
  letter-spacing: 0.6px;
  border-radius: 3px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.1), 0 3px 6px rgba(0,0,0,0.1);
  border: 0;
  outline: 0;
  transition: all 0.25s;
  &.signup {
    background: $theme-signup;
  }
  &.login {
    background: $theme-login;
  }
  &.off {
    background: none;
    box-shadow: none;
    margin: 0;
    
    &.signup {
      color: $theme-signup;
    }
    &.login {
      color: $theme-login;
    }
  }
}

button:focus, button:active, button:hover {
  box-shadow: 0 4px 7px rgba(0,0,0,0.1), 0 3px 6px rgba(0,0,0,0.1);
  &.signup {
    background: $theme-signup-darken;
  }
  &.login {
    background: $theme-login-darken;
  }
  &.off {
    box-shadow: none;
    &.signup {
      color: $theme-signup;
      background: $theme-dark;
    }
    &.login {
      color: $theme-login-darken;
      background: $theme-light;
    }
  }
}
.flex {
  display: flex;
}
@media only screen and (max-width: 768px) {
  #slideBox {
    width: 80%;
    margin-left: 20%;
  }
  .signup-info, .login-info {
    display: none;
  }
}
</style>
