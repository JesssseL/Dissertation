<template>
    <div class="budget container">
        <div class="header">
          <h1> What's your budget? </h1>
          <h2> Select an option or enter your own </h2>
        </div>
        <BudgetSelect 
          :low="lowBudget"
          :mid="midBudget"
          :high="highBudget"
          :selectedMin="selectedMin"
          :selectedMax="selectedMax"
          @budgetUpdate="updateBudget" 
        />
        <AppButton 
          text="Next"
          :disabled="selectedMin === null || selectedMax === null"
          rightIcon="arrow_forward"
          @click="saveBudget"
        />
    </div>
</template>

<script>
import BudgetSelect from '../components/BudgetSelect.vue'
import AppButton from '../elements/AppButton.vue'
import { useAiStore } from '@/stores/aiStore';
import { useSearchStore } from '../stores/searchStore'
import { useDiscoveryStore } from '../stores/discoveryStore'

export default {
  name: "BudgetView",
  props: {},
  components: {
    BudgetSelect,
    AppButton,
  },
  data() {
      return {
          searchStore: useSearchStore(),
          discoveryStore: useDiscoveryStore(),
          aiStore: useAiStore(),
          selectedMin: null,
          selectedMax: null,
      };
  },
  computed: {
    lowBudget() {
      return this.discoveryStore.budgetRanges.find(
        budget => budget.label === 'Low'
      )
    },
    midBudget() {
      return this.discoveryStore.budgetRanges.find(
        budget => budget.label === 'Mid'
      )
    },
    highBudget() {
      return this.discoveryStore.budgetRanges.find(
        budget => budget.label === 'High'
      )
    },
  },
  mounted() {
      if (this.searchStore.hasBudget) {
        console.log('has budget')
        this.selectedMin = this.searchStore.minPrice
        this.selectedMax = this.searchStore.maxPrice
      } else {
        console.log('no budget')
        this.selectedMin = (this.lowBudget?.min ?? 0)
        this.selectedMax = (this.highBudget?.max ?? 9999)
        console.log(this.lowBudget?.min)
        console.log(this.highBudget?.max)
      }
  },
  methods: {
    updateBudget(event) {
      this.selectedMin = event.min;
      this.selectedMax = event.max;
    },
    saveBudget() {
      this.searchStore.setMinPrice(this.selectedMin)
      this.searchStore.setMaxPrice(this.selectedMax)
      this.aiStore.sendStatusMessage('user', `Search Budget set to: £${this.selectedMin}-£${this.selectedMax}`)
      this.$router.push('/loading/results')
    }
  },
};
</script>

<style scoped>
.budget {
  display: flex;
  flex-direction: column;
  gap: 5px;
}
button {
  align-self: flex-end;
}
</style>