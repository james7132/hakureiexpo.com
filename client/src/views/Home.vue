<template>
<b-container>
  <h1>Test Hakurei Expo Site</h1>
  <ul>
    <li v-for='item in links'>
      <router-link :to='item.link'>
        <span> {{ item.text }}</span>
      </router-link>
    </li>
  </ul>
</b-container>
</template>

<script>
export default {
  data: function () {
    return {
      links: [
        {
          text: 'Test Post View',
          link: 'post'
        }
      ]
    }
  }
}
</script>
