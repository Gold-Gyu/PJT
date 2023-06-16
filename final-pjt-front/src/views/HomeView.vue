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
                  <span>M</span><span>O</span><span>V</span><span>l</span><span>E</span><span>W</span><br />
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
};
</script>

<style lang="scss">


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


</style>
