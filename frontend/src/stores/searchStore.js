import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

/**
 * Stores user search input and filters.
 * Acts as the "inputs" of the search flow.
 */
export const useSearchStore = defineStore('search', () => {
  const query = ref('')
  const minPrice = ref(null)
  const maxPrice = ref(null)
  const features = ref([])

  const hasQuery = computed(() => query.value.trim().length > 0)
  const hasBudget = computed(() => minPrice.value !== null && maxPrice.value !== null)

  function setQuery(value) { query.value = value }
  function setMinPrice(value) { minPrice.value = value }
  function setMaxPrice(value) { maxPrice.value = value }
  function setFeatures(value) { features.value = value }

  function clearStore() {
    query.value = ''
    minPrice.value = null
    maxPrice.value = null
    features.value = []
  }

  return {
    query,
    minPrice,
    maxPrice,
    features,
    hasQuery,
    hasBudget,
    setQuery,
    setMinPrice,
    setMaxPrice,
    setFeatures,
    clearStore
  }
})