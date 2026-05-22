import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

/**
 * Stores API results for product discovery.
 * Represents the "guildance" of the search flow.
 */
export const useDiscoveryStore = defineStore('discovery', () => {
  const intentStyle = ref("Features")
  const budgetRanges = ref([])

  const commonFeatures = ref([])
  const questions = ref([])
  const photos = ref([])

  const hasIntent = computed(() => commonFeatures.value.length > 0 || questions.value.length > 0 || photos.value.length > 0)
  const hasBudget = computed(() => budgetRanges.value.length > 0)

  function setBudgetRanges(value) { budgetRanges.value = value }
  function setFeatures(value) { commonFeatures.value = value }
  function setQuestions(value) { questions.value = value }
  function setPhotos(value) { photos.value - value }

  function clearStore() {
    commonFeatures.value = []
    budgetRanges.value = []
  }

  return {
    intentStyle,
    budgetRanges,
    commonFeatures,
    questions,
    photos,
    hasIntent,
    hasBudget,
    setBudgetRanges,
    setFeatures,
    setQuestions,
    setPhotos,
    clearStore
  }
})