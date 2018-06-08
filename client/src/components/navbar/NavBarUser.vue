<template>
<!-- Authenticated aligned nav items -->
<b-navbar-nav class="ml-auto" v-if="currentUser">
  <b-nav-item-dropdown right>
    <!-- Using button-content slot -->
    <template slot="button-content">
      <em id="create-dropdown">+</em>
    </template>
    <b-dropdown-item href="#">New Work</b-dropdown-item>
    <b-dropdown-item href="#">New Circle</b-dropdown-item>
  </b-nav-item-dropdown>

  <b-nav-item-dropdown right no-caret>
    <!-- Using button-content slot -->
    <template slot="button-content">
      <b-img :src="avatarUrl" id="avatar"/>
    </template>
    <b-dropdown-item href="#">Profile</b-dropdown-item>
    <b-dropdown-item v-on:click="logout">Logout</b-dropdown-item>
  </b-nav-item-dropdown>
</b-navbar-nav>
<!-- Unauthenticated right aligned nav items -->
<b-navbar-nav class="ml-auto" v-else>
  <b-nav-item to="/login">Login</b-nav-item>
  <b-nav-item to="/register">Sign Up</b-nav-item>
</b-navbar-nav>
</template>

<script>
import firebase from 'firebase/app'
import 'firebase/auth'

function getDisplayName (user) {
  if (user === null) {
    return ''
  }
  return user.displayName || user.email
}

let data = {}

let vm = {
  name: 'NavBarItems',
  data: function () {
    let user = firebase.auth().currentUser
    return (data = {
      currentUser: user,
      displayName: getDisplayName(user)
    })
  },
  computed: {
    avatarUrl: function () {
      return this.currentUser.photoURL || require('@/static/img/avatar_default.jpg')
    }
  },
  methods: {
    logout: () => firebase.auth().signOut()
  },
  created: function () {
    firebase.auth().onAuthStateChanged(function (user) {
      data.currentUser = user
      data.displayName = getDisplayName(user)
    })
  }
}
export default vm
</script>

<style scoped lang="scss">
#avatar {
  width: 30px;
  height: 30px;
  border-radius: 50%;
}

#create-dropdown {
  font-size: 20px;
  font-weight: bold;
}
</style>
