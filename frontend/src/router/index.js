import { createRouter, createWebHistory } from 'vue-router'
import { useSearchStore } from '../stores/searchStore.js'

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
    meta: { 
      requiresQuery: true,
     }
  },
  {
    path: '/results',
    name: 'Results',
    component: ResultsView,
    meta: { 
      requiresQuery: true, 
      requiresBudget: true
    }
  },
  {
    path: '/loading/intent',
    name: 'LoadingIntent',
    component: LoadingView,
    meta: {
      loadingType: 'intent',
      requiresQuery: true
    }
  },
  {
    path: '/loading/results',
    name: 'LoadingResults',
    component: LoadingView,
    meta: {
      loadingType: 'results',
      requiresQuery: true,
      requiresBudget: true,
    }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to) => {
  const searchStore = useSearchStore()

  if (to.meta.requiresQuery && !searchStore.hasQuery) {
    console.warn('❌ BLOCKED: requiresQuery failed → redirect /') 
    return '/'
  }
  if (to.meta.requiresBudget && !searchStore.hasBudget) {
    console.warn('❌ BLOCKED: requiresQuery failed → redirect /') 
    return '/budget'
  }

  return true
})

export default router