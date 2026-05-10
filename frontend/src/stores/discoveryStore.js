import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

/**
 * Stores API results for product discovery.
 * Represents the "guildance" of the search flow.
 */
export const useDiscoveryStore = defineStore('discovery', () => {
  const commonFeatures = ref([])
  const budgetRanges = ref([])

  const hasFeatures = computed(() => commonFeatures.value.length > 0)
  const hasBudget = computed(() => budgetRanges.value.length > 0)

  function setFeatures(value) { commonFeatures.value = value }
  function setBudgetRanges(value) { budgetRanges.value = value }

  function clearStore() {
    commonFeatures.value = []
    budgetRanges.value = []
  }

  return {
    commonFeatures,
    budgetRanges,
    hasFeatures,
    hasBudget,
    setFeatures,
    setBudgetRanges,
    clearStore
  }
})