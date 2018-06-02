import firebase from 'firebase/app'
import 'firebase/auth'

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

export default firebase
