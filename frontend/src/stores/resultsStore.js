import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

/**
 * Stores API results for product search.
 * Represents the "output" of the search flow.
 */
export const useResultsStore = defineStore('results', () => {
  const results = ref([])
  const relevantFeatures = ref([])

  const hasResults = computed(() => results.value.length > 0)

  function setResults(value) { results.value = value }
  function setFeatures(value) { relevantFeatures.value = value}

  function clearStore() {
    results.value = []
  }

  return {
    results,
    relevantFeatures,
    hasResults,
    setResults,
    setFeatures,
    clearStore
  }
})