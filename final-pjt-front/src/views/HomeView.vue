<template>
  <div>
   
    <div class="section full-height">
      <div class="absolute-center">
        <div class="section">
          <div class="container">
            <div class="row">
              <div class="col-12">
                <h1>
                  <span>W</span><span>E</span><span>L</span><span>C</span
                  ><span>O</span><span>M</span><span>E</span>
                  <span></span><br />
                  <span>T</span
                  ><span>O</span> <span></span><br />
                  <span>R</span><span>e</span><span>a</span><span>l</span><span></span><br />
                  <span>W</span><span>O</span><span>R</span><span>L</span><span>D</span>
                </h1>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      headerClass: "start-style",
      isDarkMode: false,
      stopped: false,
      secondHandTransform: "",
      minuteHandTransform: "",
      hourHandTransform: "",
    };
  },
  mounted() {
    window.addEventListener("scroll", this.handleScroll);
    this.animateHero()
    this.updateClockHands();
    setInterval(this.updateClockHands, 100);
    setTimeout(() => {
      this.stopClock();
    }, 5000);
  },
  beforeDestroy() {
    window.removeEventListener("scroll", this.handleScroll);
  },
  methods: {
    handleScroll() {
      const scroll = window.scrollY;
      if (scroll >= 10) {
        this.headerClass = "scroll-on";
      } else {
        this.headerClass = "start-style";
      }
    },
    animateHero() {
      this.$nextTick(() => {
        this.$el.classList.remove("hero-anime");
      });
    },
    toggleDarkMode() {
      this.isDarkMode = !this.isDarkMode;
    },
    updateClockHands() {
      const date = new Date();
      const seconds = date.getSeconds();
      const minutes = date.getMinutes();
      const hours = date.getHours();

      const secondHandAngle = (seconds / 60) * 360;
      this.secondHandTransform = `rotate(${secondHandAngle}deg)`;

      const minuteHandAngle = (minutes / 60) * 360 + (seconds / 60) * 6;
      this.minuteHandTransform = `rotate(${minuteHandAngle}deg)`;

      const hourHandAngle = (hours / 12) * 360 + (minutes / 60) * 30;
      this.hourHandTransform = `rotate(${hourHandAngle}deg)`;
    },

    stopClock() {
      this.stopped = true;
    },

    getCurrentTime() {
      const date = new Date();
      const hours = date.getHours();
      const minutes = date.getMinutes();
      const seconds = date.getSeconds();

      return `${this.addLeadingZero(hours)}:${this.addLeadingZero(
        minutes
      )}:${this.addLeadingZero(seconds)}`;
    },

    addLeadingZero(value) {
      return value < 10 ? `0${value}` : value;
    },
  },
};
</script>

<style lang="scss">
/* Please ❤ this if you like it! */

@import url("https://fonts.googleapis.com/css?family=Poppins:100,100i,200,200i,300,300i,400,400i,500,500i,600,600i,700,700i,800,800i,900,900i&subset=devanagari,latin-ext");


/* #Media
================================================== */

@media (max-width: 767px) {
  h1 {
    font-size: 38px;
  }
  .nav-item:after {
    display: none;
  }
  .nav-item::before {
    position: absolute;
    display: block;
    top: 15px;
    left: 0;
    width: 11px;
    height: 1px;
    content: "";
    border: none;
    background-color: #000;
    vertical-align: 0;
  }
  .dropdown-toggle::after {
    position: absolute;
    display: block;
    top: 10px;
    left: -23px;
    width: 1px;
    height: 11px;
    content: "";
    border: none;
    background-color: #000;
    vertical-align: 0;
    transition: all 200ms linear;
  }
  .dropdown-toggle[aria-expanded="true"]::after {
    transform: rotate(90deg);
    opacity: 0;
  }
  .dropdown-menu {
    padding: 0 !important;
    background-color: transparent;
    box-shadow: none;
    transition: all 200ms linear;
  }
  .dropdown-toggle[aria-expanded="true"] + .dropdown-menu {
    margin-top: 10px !important;
    margin-bottom: 20px !important;
  }
  body.dark .nav-item::before {
    background-color: #fff;
  }
  body.dark .dropdown-toggle::after {
    background-color: #fff;
  }
  body.dark .dropdown-menu {
    background-color: transparent;
    box-shadow: none;
  }
}

.logo {
  position: fixed;
  bottom: 0;
  right: 0;
  // transform: translate(-50%, -50%);
  z-index: 9999;
}

.logo img {
  height: 250px;
  width: auto;
  display: block;
  /* filter: brightness(10%); */
  /* transition: all 250ms linear; */
}
// 위의 스타일을 HTML 파일에 적용하면 .logo 클래스를 가진 요소가 우측 하단에 고정되고, 이미지는 해당 스타일을 따라 크기 조정됩니다. position: fixed 속성은 요소를 고정 위치에 배치하며, bottom: 0과 right: 0 속성을 사용하여 우측 하단에 위치하도록 지정합니다. transform: translate(-50%, -50%);은 요소를 정확히 가운데로 이동시키는 역할을 합니다. z-index: 9999;는 다른 요소




body.dark .logo img {
  filter: brightness(100%);
}

.clock-container {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100vh;
}

.clock {
  width: 400px;
  height: 400px;
  border-radius: 50%;
  background-color: #fff;
  position: relative;
  box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);
  border: 2px solid rgba(100, 80, 80, 0.336);
}

.current-time {
  position: absolute;
  top: -40px;
  left: 50%;
  transform: translateX(-50%);
  font-size: 24px;
  font-weight: bold;
}

.hand1 {
  transform: rotate(30deg);
  animation: rotate1 1s linear infinite;
}

.hand2 {
  transform: rotate(60deg);
  animation: rotate2 2s linear infinite;
}

.second-hand {
  background-color: #72c2f063;
  position: absolute;
  width: 3px;
  height: 120px;
  left: calc(50% - 3px);
  top: calc(50% - 120px);
  transform-origin: bottom center;
  z-index: 1;
}

.minute-hand {
  background-color: #0808085e;
  position: absolute;
  width: 6px;
  height: 140px;
  left: calc(50% - 4px);
  top: calc(50% - 140px);
  transform-origin: bottom center;
  z-index: 2;
}

.hour-hand {
  background-color: #0808085e;
  position: absolute;
  width: 5px;
  height: 120px;
  left: calc(50% - 5px);
  top: calc(50% - 120px);
  transform-origin: bottom center;
  z-index: 3;
}

@keyframes rotate1 {
  from {
    transform: rotate(30deg);
  }

  to {
    transform: rotate(390deg);
  }
}

@keyframes rotate2 {
  from {
    transform: rotate(60deg);
  }

  to {
    transform: rotate(420deg);
  }
}

</style>
