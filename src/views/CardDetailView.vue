<template>
  <Card :id="$props.id" />
</template>

<script lang="ts">
import { defineComponent, ref, onMounted, defineProps } from 'vue'
import axios from 'axios'
import HeaderComponent from '@/components/header-component.vue'
import Card from '@/components/card-component.vue'
import FooterComponent from '@/components/footer-component.vue'

export default defineComponent({
  name: 'CardDetailView',
  components: {
    Card
  },
  setup() {
    const props = defineProps<{
      id: {
        type: number,
        required: true
      },
    }>()
  }
})
</script>

<style>
.app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

main {
  padding: 1rem;
}
</style>
