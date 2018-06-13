<template>
<a :class="classes" :href="link">
  <font-awesome-icon :icon="['fab', type]"/>
</a>
</template>

<script>
import FontAwesomeIcon from '@fortawesome/vue-fontawesome'

let validTypes = ['facebook']

export default {
  props: ['type', 'link'],
  components: {
    FontAwesomeIcon
  },
  computed: {
    classes: function () {
      return validTypes.includes(this.type) ? this.type : 'social-icon'
    }
  }
}
</script>

<style lang="scss">
%social-icon {
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

.social-icon {
  @extend %social-icon;
}

.facebook {
  @extend %social-icon;
  background-color: blue;
}
</style>
