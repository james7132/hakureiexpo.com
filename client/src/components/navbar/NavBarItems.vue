<template>
<b-navbar-nav>
  <!-- Search -->
  <b-nav-form right class="my-auto">
    <b-input-group>
      <b-form-input size="sm" type="search" placeholder="Search"/>
      <b-input-group-append>
        <b-btn>
          <font-awesome-icon icon="search" />
        </b-btn>
      </b-input-group-append>
    </b-input-group>
  </b-nav-form>
  <b-nav-item class="nav-item" to="/circles">Circles</b-nav-item>
</b-navbar-nav>
</template>

<script>
import FontAwesomeIcon from '@fortawesome/vue-fontawesome'

export default {
  components: {
    FontAwesomeIcon
  }
}
</script>

<style>
.nav-item {
  font-weight: bold;
}
</style>
