<template>
<div>
  <h1 id="title" class="margin-split">{{ title }}</h1>
  <div class="margin-split">
    <b-img src="http://via.placeholder.com/400x300" fluid/>
  </div>
  <div cljss="margin-split">
    <b-btn>
     <font-awesome-icon icon="star" />
    </b-btn>
    <b-btn>
      <font-awesome-icon icon="share" />
    </b-btn>
    <b-btn>
      <font-awesome-icon icon="download" />
    </b-btn>
  </div>
  <vue-markdown class="margin-split" :source="description"/>
  <div class="tag" v-for="tag in tags">
    {{ tag }}
  </div>
</div>
</template>

<script>
import FontAwesomeIcon from '@fortawesome/vue-fontawesome'
import VueMarkdown from 'vue-markdown'

export default {
  props: ['title', 'tags', 'description'],
  components: {
    VueMarkdown,
    FontAwesomeIcon
  }
}
</script>

<style scoped>
button {
  margin-right: 2%;
  margin-bottom: 2%;
}

#title {
  margin-top: 2.5%;
  margin-bottom: 2.5%;
}

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
