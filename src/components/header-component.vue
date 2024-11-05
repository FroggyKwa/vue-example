<template>
  <header class="header" title="">
    <h1>{{ title }}</h1>
  </header>
</template>

<script setup lang="ts">
import { defineProps } from 'vue';

const props = defineProps({
  title: {
    type: String,
    required: true
  }
});
</script>

<style scoped style lang="stylus">

.header
  background-color #4CAF50
  color white
  text-align center
  padding 1rem
  font-family "JetBrains Mono", monospace

</style>
