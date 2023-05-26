<template>
  <div class="not-found-container">
    <h1 class="not-found-title">404 Not Found</h1>
    <h2 class="not-found-description">존재하지 않는 페이지입니다.</h2>
  </div>
</template>

<script>
export default {
  name: "NotFound404",
};
</script>

<style>
.not-found-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
}

.not-found-title {
  font-size: 48px;
  color: #ff5a5f;
  margin-bottom: 16px;
}

.not-found-description {
  font-size: 24px;
  color: #333;
}
</style>
