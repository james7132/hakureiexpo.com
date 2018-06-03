import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import Vue from 'vue'
import App from './App.vue'
import router from './router'
import firebase from './firebase.config.js'
import BootstrapVue from 'bootstrap-vue'

Vue.config.productionTip = false
Vue.use(BootstrapVue)

let app

firebase.auth().onAuthStateChanged(function (user) {
  app = app || new Vue({
    el: '#app',
    router,
    render: h => h(App)
  })
  console.log(app.api)
})
