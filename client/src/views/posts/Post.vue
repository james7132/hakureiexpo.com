<template>
  <b-container fluid>
    <b-row>
      <b-col cols='3'>
        <PostCircleView v-if='author.is_circle' v-bind='author'/>
        <PostUserView v-else v-bind='author'/>
      </b-col>
      <b-col cols='9' id='main-view'>
        <PostContentView v-bind="$data" />
      </b-col>
    </b-row>
</b-container>
</template>

<script>
import PostCircleView from '@/components/post/PostCircleView.vue'
import PostUserView from '@/components/post/PostUserView.vue'
import PostContentView from '@/components/post/PostContentView.vue'

export default {
  data: function () {
    return {
      title: 'Fantasy Crescendo',
      tags: ['Video Game', 'Touhou'],
      description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit.  Quisque tristique vel sem eget sagittis. Pellentesque interdum libero urna, a aliquam velit convallis vitae. Cras et eros ligula. Nulla facilisi. Ut eget tellus vel tellus dictum blandit. Aenean eu blandit nulla. Integer mattis quam mattis augue facilisis rhoncus. Phasellus eu odio in enim pretium placerat. Nam mattis, ante eu rhoncus luctus, odio leo venenatis sem, non condimentum felis felis vitae libero.",
      author: {
        is_circle: false,
        name: 'james7132',
        occupation: 'Programmer',
        avatar_url: null
      }
    }
  },
  components: {
    PostUserView,
    PostCircleView,
    PostContentView
  }
}
</script>

<style>
</style>
