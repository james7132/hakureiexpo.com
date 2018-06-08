import firebase from 'firebase/app'
import 'firebase/auth'

import api from './api'

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
// Set up changing
firebase.auth().onAuthStateChanged(async function (user) {
  let headers = api.http.defaults.headers.common
  if (user) {
    try {
      let token = await user.getIdToken()
      headers['Authorization'] = `Bearer ${token}`
    } catch (err) {
      console.error(err)
    }
  } else {
    delete headers['Authorization']
  }
})

export default firebase
