<template>
  <div class="app">
    <router-link to="/">
      <header-component title="Vue practice" />
    </router-link>
    <main>
      <router-view />
    </main>
    <footer-component />
  </div>
</template>

<script setup lang="ts">
import HeaderComponent from '@/components/header-component.vue'
import FooterComponent from '@/components/footer-component.vue'
</script>

<style lang="stylus">
*
  text-decoration none

* a
  color #000
.app
  display flex
  flex-direction column
  min-height 100vh

main
  padding 1rem
  flex 1

</style>
