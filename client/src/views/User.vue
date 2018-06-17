<template>
<b-container class='text-center'>
  <Avatar id='avatar' :src='avatar_url' />
  <h1>{{ display_name }}</h1>
  <h2 v-if='occupation'>{{ occupation }}</h2>
  <div id="social-media">
    <SocialMediaButton v-for='(link, type) in social_media'
      :type='type' :link='link'/>
  </div>
  <div id="bio">
    {{ bio }}
  </div>
  <div id="circles">
    <a :href="circle" v-for="circle in circles">{{ circle }}</a>
  </div>
  <b-row>
    <b-col v-for="post in posts" cols="4" class="col-centered">
      <b-card :title="post.title">

      </b-card> 
    </b-col>
  </b-row>
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
      },
      bio: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae condimentum erat, quis tempor massa. Integer quis purus sed nisi egestas mattis a sed magna. Aliquam ut quam blandit, volutpat enim vel, viverra dui. Vestibulum auctor nisl turpis, at porta arcu maximus ut. Mauris sagittis congue nunc id eleifend. Duis. ",
      circles: [
        'HouraiTeahouse',
        'NitorInc',
        'MysteryParifait'
      ],
      posts: [
        { title: 'Fantasy Crescendo' },
        { title: 'Fantasy Crescendo' },
        { title: 'Fantasy Crescendo' },
        { title: 'Fantasy Crescendo' },
        { title: 'Fantasy Crescendo' },
        { title: 'Fantasy Crescendo' },
        { title: 'Fantasy Crescendo' },
        { title: 'Fantasy Crescendo' },
      ]
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

#circles {
  margin-top: 5px;
}

#circles > a {
  padding-right: 5px;
}

#circles > a + a {
  padding-left: 5px;
  border-width: 2px;
  border-left-style: solid;
  border-color: black;
}

.col-centered {
  float: none;
  margin: 0 auto;
}
</style>
