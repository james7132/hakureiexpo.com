<template>
<b-container class='text-center'>
  <row>
    <Avatar id='avatar' :src='avatar_url' />
    <h1>{{ display_name }}</h1>
    <h2 v-if='occupation'>{{ occupation }}</h2>
    <div id="social-media">
      <SocialMediaButton v-for='(link, type) in social_media'
        :type='type' :link='link'/>
    </div>
  </row>
</b-container>
</template>

<script>
import Avatar from '@/components/user/Avatar.vue'
import SocialMediaButton from '@/components/user/SocialMediaButton.vue'

export default {
  data: function () {
    return {
      display_name: 'james7132',
      occupation: 'Programmer',
      avatar_url: null,
      social_media: {
        facebook: 'https://facebook.com/james7132',
        twitter: 'https://twitter.com/james7132',
        google: 'https://plus.google.com/james7132',
        tumblr: 'https://plus.google.com/james7132',
        github: 'https://github.com/james7132',
        patreon: 'https://patreon.com/james7132'
      }
    }
  },
  components: {
    Avatar,
    SocialMediaButton
  }
}
</script>

<style scoped>
#avatar {
  margin-left: auto;
  margin-right: auto;
}

#social-media > a + a {
  margin-left: 5px;
}
</style>
