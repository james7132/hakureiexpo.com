<template>
<b-navbar toggleable="md" type="dark" variant="dark">
  <b-container>
    <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>
    <b-navbar-brand to="/">Hakurei Expo</b-navbar-brand>
    <b-collapse is-nav id="nav_collapse">
      <NavBarItems/>
      <NavBarUser/>
    </b-collapse>
  </b-container>
</b-navbar>
</template>

<script>
import NavBarItems from '@/components/navbar/NavBarItems.vue'
import NavBarUser from '@/components/navbar/NavBarUser.vue'

export default {
  components: {
    NavBarItems,
    NavBarUser
  }
}
</script>
