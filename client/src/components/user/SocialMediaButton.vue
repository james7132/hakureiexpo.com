<template>
<a :class="['social-icon', type]" :href="link">
  <font-awesome-icon :icon="['fab', brand]"/>
</a>
</template>

<script>
import FontAwesomeIcon from '@fortawesome/vue-fontawesome'

let brands = new Map([
  ['facebook', 'facebook-f']
])

export default {
  props: ['type', 'link'],
  components: {
    FontAwesomeIcon
  },
  computed: {
    brand: function() {
      return brands.get(this.type) || this.type
    }
  }
}
</script>

<style lang="scss">
.social-icon {
  display: inline-block;
  border-radius: 50%;
  width: 50px;
  height: 50px;
  line-height: 50px;
  font-size: 1.5rem;
  background-color: #AAA;
  text-align: center;
  color: white;
}

.facebook {
  background-color: #3B5998;
}

.twitter {
  background-color: #55ACEE;
}

.google {
  background-color: #dd4b39;
}

.tumblr {
  background-color: #2c4762;
}

.github {
  background-color: #4183C4;
}

.patreon {
  background-color: #F96854;
}
</style>
