<template>
  <div>
    <p>Текущий счётчик: {{ counter }}</p>
    <p>Текущий счётчик ** 2: {{ counter_pow2 }}</p>
    <p>Текущий счётчик ** 2: {{ counter_pow2 }}</p>

<!--    <p>Текущий счётчик ** 2: {{ counter_pow2_f() }}</p>-->
<!--    <p>Текущий счётчик ** 2: {{ counter_pow2_f() }}</p>-->
    <button @click="incrementCounter">Увеличить счётчик</button>
  </div>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue'

const counter = ref(0);

function incrementCounter() {
  counter.value += 1;
}

const counter_pow2 = computed(() => {
  console.log("counted");
  return counter.value ** 2;
})

function counter_pow2_f() {
  console.log("counted");
  return counter.value ** 2
}

</script>
