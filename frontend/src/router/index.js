import { createRouter, createWebHistory } from 'vue-router'

import HomeView from '../views/HomeView.vue'
import BudgetView from '../views/BudgetView.vue'
import ResultsView from '../views/ResultsView.vue'
import LoadingView from '../views/LoadingView.vue'

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
  },
  {
    path: '/loading/:type',
    name: 'Loading',
    component: LoadingView,
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router