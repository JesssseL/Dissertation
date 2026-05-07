<template>
    <div class="budget container">
        <div class="header">
          <h1> What's your budget? </h1>
          <h2> Select an option or enter your own </h2>
        </div>
        <BudgetSelect 
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
import { useSearchStore } from '../stores/searchStore'

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
          selectedMin: null,
          selectedMax: null,
      };
  },
  mounted() {
      this.selectedMin = this.searchStore.minPrice
      this.selectedMax = this.searchStore.maxPrice
  },
  methods: {
    updateBudget(event) {
      this.selectedMin = event.min;
      this.selectedMax = event.max;
    },
    saveBudget() {
      this.searchStore.setMinPrice(this.selectedMin)
      this.searchStore.setMaxPrice(this.selectedMax)
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