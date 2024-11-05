<template>
  <router-link v-for="card in cards" :key="card.id" :to="{ name: 'card', params: { id: card.id } }">
    <Card :id="card.id" />
  </router-link>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue'
import axios from 'axios'
import Card from '@/components/card-component.vue'

export default defineComponent({
  name: 'HomeView',
  components: {
    Card
  },
  setup() {
    const cards = ref([])

    // Загружаем данные при монтировании компонента
    onMounted(async () => {
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/data')
        cards.value = response.data.cards
      } catch (error) {
        console.error('Ошибка при получении данных:', error)
      }
    })

    return {
      cards
    }
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
