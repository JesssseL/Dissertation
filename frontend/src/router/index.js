import { createRouter, createWebHistory } from 'vue-router'

import HomeView from '../views/HomeView.vue'
import BudgetView from '../views/BudgetView.vue'
import ResultsView from '../views/ResultsView.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeView
  },
  {
    path: '/budget',
    name: 'Budget',
    component: BudgetView,
  },
  {
    path: '/results',
    name: 'Results',
    component: ResultsView
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router