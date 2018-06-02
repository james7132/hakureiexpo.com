import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import Vue from 'vue'
import App from './App.vue'
import router from './router'
import BootstrapVue from 'bootstrap-vue'

import firebase from 'firebase/app'
import 'firebase/auth'

Vue.config.productionTip = false
Vue.use(BootstrapVue)

let app

// TODO(james7132): Move this to some configuraiton file
// Initialize Firebase
var config = {
  apiKey: 'AIzaSyCsUCEAOOOwaZ5Xzrko-htdmzh0lMMZXgM',
  authDomain: 'hakurei-expo.firebaseapp.com',
  databaseURL: 'https://hakurei-expo.firebaseio.com',
  projectId: 'hakurei-expo',
  storageBucket: 'hakurei-expo.appspot.com',
  messagingSenderId: '477820962691'
}
firebase.initializeApp(config)
firebase.auth().onAuthStateChanged(function (user) {
  if (app) return
  app = new Vue({
    router,
    render: h => h(App)
  })
  app.$mount('#app')
})
