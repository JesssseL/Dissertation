import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useSearchStore = defineStore('search', () => {
  const query = ref('')
  const minPrice = ref(0)
  const maxPrice = ref(0)

  function setQuery(value) {
    query.value = value
  }

  function setMinPrice(value) {
    minPrice.value = value
  }

  function setMaxPrice(value) {
    maxPrice.value = value
  }

  function clearStore() {
    query.value = ''
  }

  return {
    query,
    minPrice,
    maxPrice,
    setQuery,
    setMinPrice,
    setMaxPrice,
    clearStore
  }
})