<template>
<div>
  <h1>{{ title }}</h1>
  <div class="margin-split">
    <b-img src="http://via.placeholder.com/400x300" fluid/>
  </div>
  <vue-markdown class="margin-split" :source="description"/>
  <div class="tag" v-for="tag in tags">
    {{ tag }}
  </div>
</div>
</template>

<script>
import VueMarkdown from 'vue-markdown'

export default {
  props: ['title', 'tags', 'description'],
  components: {
    VueMarkdown
  }
}
</script>

<style>
.margin-split {
  margin-bottom: 2.5%;
}

.tag {
  float: left;
  color: #fff;
  background: #bb7777;
  border-radius: 20px;
  margin-right: 1px;
  margin-bottom: 1px;
  padding-left: 10px;
  padding-right: 10px;
}
</style>
