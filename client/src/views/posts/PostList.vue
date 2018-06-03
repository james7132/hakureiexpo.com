<template>
  <b-container>
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
  async created () {
    try {
      this.$data.items = (await api.post.list()).data
    } catch (err) {
      console.log(err)
    }
  }
}
</script>
