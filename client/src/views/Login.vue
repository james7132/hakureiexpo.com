<template>
<div id='login' class='container'>
  <br>
  <h3>Sign In</h3>
  <b-input type='text' v-model="email" placeholder='Email'></b-input><br>
  <b-input type='password' v-model="password" placeholder='Password'></b-input><br>
  <b-button v-on:click="login">Connection</b-button>
  <p>Don't have an account? <b-link to='register'>Sign up!</b-link></p>
</div>
</template>

<script>
import firebase from 'firebase/app'
import 'firebase/auth'

export default {
  name: 'login',
  data: function () {
    return {
      email: '',
      password: ''
    }
  },
  methods: {
    login: function () {
      console.log('hello login')
      firebase.auth().signInWithEmailAndPassword(this.email, this.password)
        .then(
          function (user) {
            alert(`Welcome! ${user}!`)
            console.dir(user)
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
