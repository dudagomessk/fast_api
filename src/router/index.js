import { createRouter, createWebHistory } from 'vue-router'
import TutoresView from '../views/TutoresView.vue'
import PetsView from '../views/PetsView.vue'

const routes = [
  { path: '/', redirect: '/tutores' },
  { path: '/tutores', component: TutoresView },
  { path: '/pets', component: PetsView },
]

export default createRouter({
  history: createWebHistory(),
  routes,
})