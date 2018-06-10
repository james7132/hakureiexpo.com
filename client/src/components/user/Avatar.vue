<template>
<b-img :src='avatarUrl' class='avatar' :width='width' :height='height'/>
</template>

<script>
export default {
  name: 'Avatar',
  props: {
    src: {
      default: null,
      type: String
    },
    width: {
      default: '100%',
      type: String
    },
    height: {
      default: '100%',
      type: String
    }
  },
  computed: {
    avatarUrl: function () {
      return this.src || require('@/static/img/avatar_default.jpg')
    }
  }
}
</script>

<style>
.avatar {
  border-radius: 50%;
}
</style>
