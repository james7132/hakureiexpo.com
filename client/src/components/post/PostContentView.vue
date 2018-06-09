<template>
<div>
  <h1>{{ title }}</h1>
  <div class="margin-split">
    <b-img src="http://via.placeholder.com/400x300" fluid/>
  </div>
  <div class="margin-split">
    {{ description }}
  </div>
  <div class="tag" v-for="tag in tags">
    {{ tag }}
  </div>
</div>
</template>

<script>
export default {
  props: ['title', 'tags', 'description']
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
