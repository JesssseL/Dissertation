<template>
    <div class="saved-products container">
        <div class="header">
          <h1> Products you have saved </h1>
          <h2> From all your searches </h2>
        </div>

        <div
          class="product-cards saved-product-cards">
            <ProductCard 
              v-for="product in savedProducts"
              :key="product.id"
              :name="product.name"
              :brand="product.brand"
              :rating="product.rating"
              :image="product.image"
              :webUrl="product.webUrl"
              :price="product.price"
              :tag="product.tag"
              theme="saved"
            />
        </div>

        <div class="saved-products-footer footer">
            <AppButton 
                text="Back to Search"
                leftIcon="arrow_back"
                @click="newSearch"
            />
        </div>
    </div>
</template>

<script>
import ProductCard from '../components/ProductCard.vue'
import AppButton from '../elements/AppButton.vue'
import { useAccountStore } from '@/stores/accountStore.js';
import { getProducts } from '@/services/databaseService.js';

export default {
  name: "SavedProducts",
  components: {
    ProductCard,
    AppButton,
  },
  data() {
    return {
      accountStore: useAccountStore(),
      savedProducts: [],
    };
  },
  async mounted() {
    const response = await this.getSavedProducts()
    this.savedProducts = response.account_products
    console.log(this.savedProducts)
  },
  methods: {
    async getSavedProducts() {
      try {
        console.log('started to get products')
            return await getProducts(
                this.accountStore.email,
                this.accountStore.password,
            )
        } catch (error) {
            console.error('Failed to save product:', error)
            alert('Could not load products')
            return false
        }
    },
    newSearch() {
      this.searchStore.clearStore()
      this.$router.push('/')
    },
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

.saved-product-cards {
  display: flex;
  flex-direction: column;
  gap: 5px;
  height: 100%;
  margin: 0 auto;
  align-items: center;
}

.saved-products-footer {
    margin-top: auto;
}
</style>