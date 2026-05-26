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
  const questionsAndAnswers = ref([]) //Intent specific
  const photos = ref([]) //Intent specific

  const hasQuery = computed(() => query.value.trim().length > 0)
  const hasBudget = computed(() => minPrice.value !== null && maxPrice.value !== null)

  function setQuery(value) { query.value = value }
  function setMinPrice(value) { minPrice.value = value }
  function setMaxPrice(value) { maxPrice.value = value }
  function setFeatures(value) { features.value = value }
  function addFeature(value) { features.value.push(value) }
  function removeFeature(value) { features.value.splice(features.value.indexOf(value), 1) }
  function addQuestionsAndAnswers(value) { questionsAndAnswers.value = value }  //Intent specific
  function addPhotos(value) { addPhotos.value = value } //Intent specific

  function clearStore() {
    query.value = ''
    minPrice.value = null
    maxPrice.value = null
    features.value = []
    questionsAndAnswers.value = []
    photos.value = []
  }

  return {
    query,
    minPrice,
    maxPrice,
    features,
    questionsAndAnswers,  //Intent specific
    photos, //Intent specific
    hasQuery,
    hasBudget,
    setQuery,
    setMinPrice,
    setMaxPrice,
    setFeatures,
    addFeature,
    removeFeature,
    addQuestionsAndAnswers,  //Intent specific
    addPhotos, //Intent specific
    clearStore
  }
})