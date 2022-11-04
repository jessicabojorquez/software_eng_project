<script>
export default {
  props:{
    msgClicked: String,
    msgNotClicked: String,
  },
  data() {
    return {
      isClicked: false
    }
  },
  methods: {
    toggle() {
      this.isClicked = !this.isClicked
    }
  }
}
</script>

<template>
  <button @click="toggle" v-if="isClicked">{{msgClicked || "something"}}</button>
  <button @click="toggle" v-else>{{msgNotClicked ||"nothing"}}</button>
</template>