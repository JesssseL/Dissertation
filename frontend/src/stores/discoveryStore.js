import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

/**
 * Stores API results for product discovery.
 * Represents the "guildance" of the search flow.
 */
export const useDiscoveryStore = defineStore('discovery', () => {
  const budgetRanges = ref([])
  const questions = ref([])

  const hasIntent = computed(() => questions.value.length)
  const hasBudget = computed(() => budgetRanges.value.length > 0)

  function setBudgetRanges(value) { budgetRanges.value = value }
  function setQuestions(value) { questions.value = value }

  function clearStore() {
    questions.value = []
    budgetRanges.value = []
  }

  return {
    budgetRanges,
    questions,
    hasIntent,
    hasBudget,
    setBudgetRanges,
    setQuestions,
    clearStore
  }
})