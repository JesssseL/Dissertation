<template>
    <div class="results container">
        <div class="header">
          <h1> Top Picks for you </h1>
          <h2> Based on your search for 
            <span class="accent">{{searchStore.query}}</span>
          </h2>
        </div>

        <div class="background-gradient">
          Chat about these options with AI
        </div>
        
        <div class="product-cards">
            <ProductCard 
              v-for="product in productSuggestions"
              :key="product.id"
              :name="product.name" 
              :image="product.image" 
              :features="product.features" 
              :additionalFeatures="product.additionalFeatures" 
              :webUrl="product.webUrl"
              :price="product.price"
              :selectedFeatures="searchFeatures"
              @toggleFeature="addSearchFeature"
            />
        </div>

        <div class="results-footer footer">
            <AppButton 
                text="New Search"
                leftIcon="arrow_back"
                @click="newSearch"
            />
            <AppButton 
                text="Regenerate"
                leftIcon="wand_stars"
                :disabled="!featuresChanged"
                @click="regenerateSearch"
            />
            <AppButton
                text="Refine Search"
                leftIcon="search"
                @click="refineSearch"
            />
        </div>
    </div>
</template>

<script>
import ProductCard from '../components/ProductCard.vue'
import AppButton from '../elements/AppButton.vue'
import { useSearchStore } from '../stores/searchStore'
import { useResultsStore } from '../stores/resultsStore'

export default {
  name: "ResultsView",
  props: {},
  components: {
    ProductCard,
    AppButton,
  },
  data() {
    return {
      searchStore: useSearchStore(),
      resultsStore: useResultsStore(),
      productSuggestions: [],
      searchFeatures: [],
      initialFeatures: [],
    };
  },
  computed: {
    featuresChanged() {
      return JSON.stringify(this.initialFeatures) !== JSON.stringify(this.searchFeatures)
    }
  },
  mounted() {
    this.productSuggestions = this.resultsStore.results
    this.searchFeatures = [...this.searchStore.features]
    this.initialFeatures = [...this.searchStore.features]
  },
  methods: {
    addSearchFeature(feature) {
      if (this.searchFeatures.includes(feature)) {
        this.searchStore.removeFeature(feature)
      }
      else {
        this.searchStore.addFeature(feature)
      }
      this.searchFeatures = this.searchStore.features
    },
    newSearch() {
      this.searchStore.clearStore()
      this.$router.push('/')
    },
    regenerateSearch() {
      this.$router.push('/loading')
    },
    refineSearch() {
      this.$router.push('/budget')
    }
  },
};
</script>

<style scoped>
.product-cards {
    display: flex;
    gap: 10px;
    width: 100%;
    flex: 1;
}

.results {
  display: flex;
  flex-direction: column;
  gap: 5px;
  height: 100%;
}

.results-footer {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: center;
    width: 100%;
    gap: var(--gap);
    padding: var(--padding);
}
</style>