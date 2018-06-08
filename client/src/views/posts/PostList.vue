<template>
  <b-container>
    <b-button v-on:click="refresh">Refresh</b-button></br>
    <b-table hover :items='items'></b-table>
  </b-container>
</template>

<script>
import api from '../../api'

export default {
  data: function () {
    return {
      fields: ['name', 'creator', 'type'],
      items: []
    }
  },
  methods: {
    async refresh () {
      try {
        //console.log(api.http.defaults.headers.common['Authorization'])
        this.$data.items = (await api.post.list()).data
      } catch (err) {
        console.log(err)
      }
    }
  },
  async created () {
    try {
      //console.log(api.http.defaults.headers.common['Authorization'])
      this.$data.items = (await api.post.list()).data
    } catch (err) {
      console.log(err)
    }
  }
}
</script>
