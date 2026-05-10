<template>
    <section class="container loading-page">
      <div class="loading-content">
        <span class="material-symbols-outlined loading-icon">
          shopping_bag
        </span>

        <template v-if="loadingType === 'intent'">
          <h1 class="loading-text">
            Understanding
            <span class="accent">{{ searchStore.query }}</span>
            options...
          </h1>
          <p>Gathering information to help your choices.</p>
        </template>

        <template v-else-if="loadingType === 'results'">
          <h1 class="loading-text">
            Finding the best
            <span class="accent">{{ searchStore.query }}</span>
            for you...
          </h1>
          <p>Please wait while we personalise your recommendations.</p>
        </template>

        <template v-else>
          <h1 class="loading-text">
            Loading...
          </h1>
        </template>
      </div>
    </section>
</template>

<script>
import { useSearchStore } from '../stores/searchStore'
import { useResultsStore } from '../stores/resultsStore'
import { getProductFeatures, getBudgetRanges } from '../services/productService'
import { getRecommendations } from '../services/reccomendationService'


export default {
  name: "LoadingView",
  data() {
    return {
      searchStore: useSearchStore(),
      resultsStore: useResultsStore(),
    };
  },
  computed: {
    loadingType() {
      return this.$route.meta.loadingType
    },
  },
  async mounted() {
    if (this.loadingType === 'intent'){
      await this.getProductInfo()
      this.$router.push('/budget') //TODO - reroute to intent specification
    }
    else if (this.loadingType === 'results'){
      await this.getProductResults()
      this.$router.push('/results')
    }
    else {
      this.$router.push('/')
    }
  },
  methods: {
    async getProductInfo() {
      await Promise.all([
        getProductFeatures(),
        getBudgetRanges()
      ])

      return true
    },
    async getProductResults () {
      const results = await getRecommendations({
        productType: this.searchStore.productType,
        budgetMin: this.searchStore.budgetMin,
        budgetMax: this.searchStore.budgetMax
      })

      this.resultsStore.setResults(results)
      return true
    },
  },
};
</script>

<style scoped>
h1,
h1 * {
  font-family: var(--font-secondary);
  font-size: 4rem;
  font-weight: 400;
  line-height: 1;
  letter-spacing: -0.02em;
  text-align: center;
  display: inline;
}

.loading-page {
  display: flex;
  align-items: center;
  justify-content: center;
  pointer-events: none;
}

.loading-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: 1rem;
}

.loading-text {
    max-width: 600px;
}

p {
    color: var(--grey-text);
}

.loading-icon {
  font-size: 7rem;
  color: var(--primary);
  animation: spin 1.5s linear infinite;
}

@keyframes spin {
  from {
    transform: rotate(0deg);
  }

  to {
    transform: rotate(360deg);
  }
}
</style>