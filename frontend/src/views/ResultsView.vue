<template>
    <div class="results container">
        <div class="header">
          <h1> Top Picks for you </h1>
          <h2> Based on your search for 
            <span class="accent">{{searchStore.query}}</span>
          </h2>
        </div>
        
        <div class="product-cards">
            <ProductCard 
                name="Product Name" 
                image="https://picsum.photos/400/300" 
                :features="['Feature One', 'Feature Two', 'Feature Three', 'Feature Four']" 
                :additionalFeatures="['Feature Five', 'Feature Six', 'Feature Seven']" 
                price="999.99"
            />
            <ProductCard 
                name="Product Name" 
                image="https://picsum.photos/200/300" 
                :features="['Feature One', 'Feature Two', 'Feature Three']" 
                :additionalFeatures="['Feature Five', 'Feature Eight', 'Feature Nine', 'Feature Ten']" 
                price="999.99"
            />
            <ProductCard 
                name="Product Name" 
                image="https://picsum.photos/600/600" 
                :features="['Feature One', 'Feature Two', 'Feature Three', 'Feature Four']" 
                :additionalFeatures="['Feature Six', 'Feature Seven', 'Feature Nine', 'Feature Ten']" 
                price="999.99"
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
                :disabled="true"
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
    };
  },
  methods: {
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