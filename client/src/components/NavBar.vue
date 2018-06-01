<template>
<b-navbar toggleable="md" type="dark" variant="dark">
  <b-container>
    <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>

    <b-navbar-brand href="#">Hakurei Expo</b-navbar-brand>

    <b-collapse is-nav id="nav_collapse">

      <b-navbar-nav>
        <b-nav-form>
          <b-form-input size="sm" class="mr-sm-2" type="text" placeholder="Search"/>
        </b-nav-form>
        <b-nav-item href="/circles">Circles</b-nav-item>
      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">

        <b-nav-item-dropdown right>
          <!-- Using button-content slot -->
          <template slot="button-content">
            <em>+</em>
          </template>
          <b-dropdown-item href="#">New Work</b-dropdown-item>
          <b-dropdown-item href="#">New Circle</b-dropdown-item>
        </b-nav-item-dropdown>

        <b-nav-item-dropdown right>
          <!-- Using button-content slot -->
          <template slot="button-content">
            <em>User</em>
          </template>
          <b-dropdown-item href="#">Profile</b-dropdown-item>
          <b-dropdown-item href="#">Signout</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>

    </b-collapse>
  </b-container>
</b-navbar>
</template>

<script>
export default {
  name: 'NavBar'
}
</script>

<style scoped lang="scss">
</style>
