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
import { useAiStore } from '@/stores/aiStore';
import { useSearchStore } from '../stores/searchStore'
import { useResultsStore } from '../stores/resultsStore'
import { useDiscoveryStore } from '../stores/discoveryStore'
import { 
  getProductPhotos, 
  getProductQuestions, 
  getProductFeatures, 
  getBudgetRanges } from '../services/productService'
import { 
  getNewQueryFromQuestionAnswers,
  getNewQueryFromPhotosSelected,
  getRecommendations } from '../services/reccomendationService'


export default {
  name: "LoadingView",
  data() {
    return {
      aiStore: useAiStore(),
      searchStore: useSearchStore(),
      resultsStore: useResultsStore(),
      discoveryStore: useDiscoveryStore(),
    };
  },
  computed: {
    loadingType() {
      return this.$route.meta.loadingType
    },
  },
  async mounted() {
    if (this.loadingType === 'intent'){
      await this.getProductInfoWithQuestions()
      this.$router.push('/questions')
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
    async getProductInfoWithQuestions() {
      try {
        const [questions, budgetRanges] = await Promise.all([
          getProductQuestions(this.searchStore.query),
          getBudgetRanges(this.searchStore.query)
        ])

        this.discoveryStore.setQuestions(questions)
        this.discoveryStore.setBudgetRanges(budgetRanges)
        return true
      } catch (error) {
        console.error('Failed to load product info:', error)
        return false
      }
    },
    async getProductResults () {
      try {
        if (this.searchStore.questionsChanged) {
          // Prevents search term being regenerated when questions have not been changed
          let questionsResponse = await getNewQueryFromQuestionAnswers(
            this.searchStore.query,
            this.searchStore.questionsAndAnswers
          )
          this.searchStore.query = questionsResponse.query
          this.searchStore.markQuestionsRead()
        }

        const results = await getRecommendations(
          this.searchStore.query, 
          this.searchStore.minPrice, 
          this.searchStore.maxPrice,
          this.searchStore.features
        )
        this.aiStore.addResults(results.search_products)
        this.resultsStore.setResults(results.search_products)
        this.resultsStore.setFeatures(results.relevant_features)
        return true
      } catch (error) {
        console.error('Failed to load product results:', error)
        return false
      }
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