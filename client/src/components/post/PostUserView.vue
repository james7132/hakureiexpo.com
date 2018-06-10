<template>
<div>
  <Avatar id="avatar" class="text-center" :src="avatar_url"/>
  <h1 class="text-center">{{ name }}</h1>
  <h2 class="text-center">{{ occupation }}</h2>
  <div>

  </div>
</div>
</template>

<script>
import Avatar from '@/components/user/Avatar.vue'

export default {
  props: ['name', 'occupation', 'avatar_url'],
  components: {
    Avatar
  }
}
</script>

<style scoped>
#avatar {
  display: block;
  margin-top: 20px;
  margin-bottom: 20px;
  margin-left: auto;
  margin-right: auto;
}
</style>
