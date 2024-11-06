<template>
  <router-link v-for="card in cards" :key="card.id" :to="{ name: 'card', params: { id: card.id } }">
    <Card :id="card.id" />
  </router-link>
</template>

<script setup lang="ts">
import { ref, onBeforeMount } from 'vue'
import axios from 'axios'
import Card from '@/components/card-component.vue'


const cards = ref([])

onBeforeMount(fetch_cards)
// onMounted(async () => {
//   await fetch_cards()
// })

async function fetch_cards() {
  try {
    const response = await axios.get('http://127.0.0.1:5000/api/data')
    cards.value = response.data.cards
  } catch (error) {
    console.error('Ошибка при получении данных:', error)
  }
}

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
