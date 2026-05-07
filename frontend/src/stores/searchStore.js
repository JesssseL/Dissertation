import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useSearchStore = defineStore('search', () => {
  const query = ref('')
  const minPrice = ref(null)
  const maxPrice = ref(null)
  const features = ref([])

  function setQuery(value) {
    query.value = value
  }

  function setMinPrice(value) {
    minPrice.value = value
  }

  function setMaxPrice(value) {
    maxPrice.value = value
  }

  function setFeatures(value) {
    features.value = value
  }

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
    setQuery,
    setMinPrice,
    setMaxPrice,
    setFeatures,
    clearStore
  }
})