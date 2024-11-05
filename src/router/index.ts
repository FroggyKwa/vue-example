import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import CardDetailView from '@/views/CardDetailView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/card/:id',
      name: 'card',
      component: CardDetailView,
      props: true,
    },
    {
      path: '/',
      name: 'home',
      component: HomeView
    }
  ]
})

export default router
