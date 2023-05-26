<template>
  <div>
    <h1> 게시물 목록 </h1>
    <ArticleListItem
    
    />
  </div>
</template>

<script>
// import axios from "axios"
import ArticleListItem from '@/components/ArticleListItem'
export default {
    name : 'ArticleList',
    components : {
      ArticleListItem
    }
    
}
</script>

<style>

</style>