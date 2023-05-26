<template>
  <div>
    <div class="cards">
      <a href="http://localhost:8080/movieAll">Movie List</a>
      <h1>야심한 밤 등골이 오싹해지는 </h1>
      <div class="card card_one">
        <div class="card__bg" @click="goToDetail"></div>
        <img class="card__img" src="" />
        <div class="card__text">
          <p class="card__title">이블 데드 라이즈</p>
        </div>
      </div>
      <div class="card card_two" @click="goToDetail2">
        <div class="card__bg"></div>
        <img class="card__img" src="" />
        <div class="card__text">
          <p class="card__title">엑소시스트: <br>더 바티칸</p>
        </div>
      </div>
      <div class="card card_three" @click="goToDetail3">
        <div class="card__bg"></div>
        <img class="card__img" src="" />
        <div class="card__text">
          <p class="card__title">렌필드</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "DawnView",
  data() {
    return {
      dawnList: null,
      slickInstance: null,
    };
  },
  created() {
    axios
      .get("http://127.0.0.1:8000/movies/genres/27/")
      .then((res) => {
        console.log(res.data);
        this.dawnList = res.data;
      })
      .catch((err) => {
        console.log(err);
      });
  },
  methods: {
    goToDetail() {
      const dawn = this.dawnList[0];
      this.$router.push({
        name: "detail",
      }),
        this.$store.dispatch("sendDetail", dawn);
    },
    goToDetail2() {
      const dawn = this.dawnList[1];
      this.$router.push({
        name: "detail",
      }),
        this.$store.dispatch("sendDetail", dawn);
    },
    goToDetail3() {
      const dawn = this.dawnList[2];
      this.$router.push({
        name: "detail",
      }),
        this.$store.dispatch("sendDetail", dawn);
    },
  },
  mounted() {
    const cards = document.querySelector(".cards");
    const images = document.querySelectorAll(".card__img");
    const backgrounds = document.querySelectorAll(".card__bg");
    const range = 40;
    const calcValue = (a, b) => ((a / b) * range - range / 2).toFixed(1); // thanks @alice-mx

    let timeout;
    document.addEventListener("mousemove", ({ x, y }) => {
      if (timeout) {
        window.cancelAnimationFrame(timeout);
      }

      timeout = window.requestAnimationFrame(() => {
        const yValue = calcValue(y, window.innerHeight);
        const xValue = calcValue(x, window.innerWidth);

        cards.style.transform = `rotateX(${yValue}deg) rotateY(${xValue}deg)`;

        [].forEach.call(images, (image) => {
          image.style.transform = `translateX(${-xValue}px) translateY(${yValue}px)`;
        });

        [].forEach.call(backgrounds, (background) => {
          background.style.backgroundPosition = `${xValue * 0.45}px ${
            -yValue * 0.45
          }px`;
        });
      });
    });
  },
};

</script>

<style>

@import url("https://fonts.googleapis.com/css?family=Open+Sans:300,400,600,700,800");
html,
body {
  height: 100%;
}

body {
  align-items: center;
  background: #642b73;
  background: linear-gradient(to bottom, #c6426e, #642b73);
  display: flex;
  font-family: "Open Sans", sans;
  justify-content: center;
  overflow: hidden;
  perspective: 1800px;
  text-align: center;
  margin: 0 20px;
}

h1 {
  color: #3e3e42;
  font-size: 32px;
  font-weight: 800;
  letter-spacing: -1px;
  margin-bottom: 30px;
  transform: translateZ(35px);
}

h3 {
  color: #eb285d;
  font-size: 16px;
  margin-bottom: 6px;
  transform: translateZ(25px);
}

.cards {
  background: #fff;
  border-radius: 15px;
  box-shadow: 0px 10px 20px 20px rgba(0, 0, 0, 0.17);
  display: inline-block;
  padding: 30px 35px;
  perspective: 1800px;
  text-align: left;
  transform-origin: 50% 50%;
  transform-style: preserve-3d;
  transform: rotateX(11deg) rotateY(16.5deg);
  min-width: 595px;
}

.card {
  border-radius: 15px;
  box-shadow: 5px 5px 20px -5px rgba(0, 0, 0, 0.6);
  cursor: pointer;
  display: inline-block;
  height: 250px;
  overflow: hidden;
  perspective: 1200px;
  position: relative;
  transform-style: preserve-3d;
  transform: translatez(35px);
  transition: transform 200ms ease-out;
  width: 175px;
  text-align: center;
}

.card__img {
  position: relative;
  height: 100%;
}

.card__bg {
  bottom: -50px;
  left: -50px;
  position: absolute;
  right: -50px;
  top: -50px;
  transform-origin: 50% 50%;
  transform: translateZ(-50px);
  z-index: 0;
}

.card_one {
  .card__img {
    top: 14px;
    right: -10px;
    height: 110%;
  }
  .card__bg {
    background: url("https://image.tmdb.org/t/p/w500/5ik4ATKmNtmJU6AYD0bLm56BCVM.jpg")
      center / cover no-repeat;
  }
  .card__text {
    background-color: #254b60;
  }
}

.card_two {
  .card__img {
    top: 25px;
  }
  .card__bg {
    background: url("https://image.tmdb.org/t/p/w500/fA1xRPplBqW87wWh0hO1pwbQmX8.jpg")
      center / cover no-repeat;
  }
  .card__text {
    background-color: #274a2e;
  }
}

.card_three {
  .card__img {
    top: 5px;
    left: -4px;
    height: 110%;
  }
  .card__bg {
    background: url("https://image.tmdb.org/t/p/w500/wJXgQ3FgVIyVUwdoaKoeobET3po.jpg")
      center / cover no-repeat;
  }
  .card__text {
    background-color: #3e2222;
  }
}

.card__text {
  align-items: center;
  background: linear-gradient(
    to bottom,
    rgba(0, 0, 0, 0) 0%,
    rgba(0, 0, 0, 0.55) 100%
  );
  bottom: 0;
  display: flex;
  flex-direction: column;
  height: 70px;
  justify-content: center;
  position: absolute;
  width: 100%;
  z-index: 2;
}

.card__title {
  color: #fff;
  font-size: 18px;
  font-weight: 700;
  padding: 0 10px;
  margin-bottom: 3px;
}

.notice {
  background: gold;
  border-top-left-radius: 6px;
  bottom: 0;
  font-family: monospace;
  font-size: 14px;
  padding: 8px 10px;
  position: absolute;
  right: -20px;
}

.twitter__link {
  cursor: pointer;
  position: absolute;
  right: -10px;
  top: 12px;
  z-index: -1;
  background: #00aced;
  border-radius: 20px;
  height: 30px;
  text-decoration: none;
  padding-right: 10px;
  justify-content: space-between;
  font-weight: 600;
  display: flex;
  align-items: center;
  color: #fff;
  font-size: 14px;
  width: 74px;
  opacity: 0.4;
}

.twitter__icon {
  height: 30px;
}
</style>
