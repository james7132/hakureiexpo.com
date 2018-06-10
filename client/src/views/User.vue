<template>
<b-container class="text-center">
  <row>
    <Avatar id="avatar" :src="avatar_url" />
    <h1>{{ display_name }}</h1>
    <h2 v-if="occupation">{{ occupation }}</h2>
  </row>
</b-container>
</template>

<script>
import Avatar from '@/components/user/Avatar.vue'

export default {
  data: function () {
    return {
      display_name: "james7132",
      occupation: "Programmer",
      avatar_url: null,
      social_media: {
        facebook: "james7132",
        github: "james7132",
        patreon: "james7132"
      }
    }
  },
  components: {
    Avatar
  }
}
</script>

<style scoped>
#avatar {
  margin-left: auto;
  margin-right: auto;
}
</style>
