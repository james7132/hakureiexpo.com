import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Login from './views/Login.vue'
import Register from './views/Register.vue'
import About from './views/About.vue'

import PostList from './views/posts/PostList.vue'
import Post from './views/posts/Post.vue'
import User from './views/User.vue'

import firebase from 'firebase/app'
import 'firebase/auth'

Vue.use(Router)

let router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/about',
      name: 'about',
      component: About
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/register',
      name: 'register',
      component: Register
    },
    {
      path: '/post',
      name: 'post',
      component: Post
    },
    {
      path: '/posts',
      name: 'postList',
      component: PostList
    },
    {
      path: '/user',
      name: 'user',
      component: User
    }
  ]
})

router.beforeEach((to, from, next) => {
  let currentUser = firebase.auth().currentUser
  let requiresAuth = to.matched.some(record => record.meta.requiresAuth)

  if (requiresAuth && !currentUser) {
    next('login')
  } else {
    next()
  }
})

export default router
