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
  {
    path: '/activities/word-by-word/play-word-by-word',
    name: 'PlayWordByWord',
    component: () => import('@/pages/play-word-by-word/PlayWordByWordPage.vue'),
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
