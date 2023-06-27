import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Main',
    component: () => import('@/pages/Main')
  },
  {
    path: '/task_one',
    name: 'TaskOne',
    component: () => import('@/pages/TaskOne')
  },
  {
    path: '/task_two',
    name: 'TaskTwo',
    component: () => import('@/pages/TaskTwo')
  }
]

const router = createRouter({
  routes,
  history: createWebHistory(process.env.BASE_URL)
})

export default router
