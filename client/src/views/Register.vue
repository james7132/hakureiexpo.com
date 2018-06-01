<template>
<div id="login" class="container">
  <br>
  <b-input type="text" v-model="email"placeholder="Email"></b-input><br>
  <b-input type="password" v-model="password" placeholder="Password"></b-input><br>
  <b-input type="password" v-model="passwordVerify" placeholder="Password Again"></b-input><br>
  <b-button v-on:click="signUp">Sign Up</b-button>
  <p>Already have an account? <b-link to="login">Log in.</b-link></p>
</div>
</template>

<script>
import firebase from 'firebase'

export default {
  name: 'register',
  data: function () {
    return {
      email: '',
      password: '',
      passwordVerify: ''
    }
  },
  methods: {
    signUp: function () {
      console.log('hello register')
      firebase.auth().createUserWithEmailAndPassword(this.email, this.password)
        .then(
          function (user) {
            alert('Your account has been created!')
          },
          function (err) {
            alert(`Error: ${err.message}`)
          }
        );
    }
  }
}
</script>

<style scoped>
#login {
  text-align: center
}
</style>
