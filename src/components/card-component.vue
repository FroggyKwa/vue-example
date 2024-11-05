<template>
  <div class="card">
    <h2>{{ title }}</h2>
    <p>{{ description }}</p>
  </div>
</template>

<script setup lang="ts">
import { defineProps, onMounted, ref } from 'vue'
import axios from 'axios'

const title = ref("");
const description = ref("");

const props = defineProps<{
  id: {
    type: number,
    required: true
  },
}>();

onMounted(async () => {
  try {
    const response = await axios.get(`http://127.0.0.1:5000/api/data/${props.id}`);
    console.log(response.data)
    title.value = response.data.title;
    description.value = response.data.description;

  } catch (error) {
    console.error("Ошибка при получении данных:", error);
  }
})
</script>

<style scoped>
.card {
  border: 1px solid #ddd;
  padding: 1rem;
  border-radius: 8px;
  margin-bottom: 1rem;
  text-align: center;
}
</style>
