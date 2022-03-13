import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/pages/home/HomePage.vue'),
  },
  {
    path: '/activities',
    name: 'activities',
    component: () => import('@/pages/activities/ActivitiesPage.vue'),
  },
  {
    path: '/activities/word-by-word',
    name: 'WordByWord',
    component: () => import('@/pages/word-by-word/WordByWordPage.vue'),
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
