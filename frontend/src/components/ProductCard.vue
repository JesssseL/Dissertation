<template>
    <article class="product-card saved-product-card">
        <div class="card-image">
            <span class="card-tag">
                <span class="button-icon material-symbols-outlined card-star card-tag__icon"> star </span>
                {{tag}}
            </span>
            <img :src="image" :alt="`Image of ${name}`" />
        </div>

        <div class="card-main-and-footer">
            <div class="card-main">
                <h2 class="card-title"> {{name}} </h2>
                <div class="card-details"> 
                    <span class="button-icon material-symbols-outlined"> sell </span>
                    <span> {{brand}} </span>
                    <hr/>
                    <span class="button-icon material-symbols-outlined card-star"> star </span>
                    <span class="card-rating"> {{rating}} </span>
                </div>

                <p class="label"
                    v-if="features.length > 0"
                >Reccomended Features</p>
                <div class="card-features">
                    <SelectableTag 
                        v-if="features.length > 0"
                        v-for="feature in features" 
                        :key="feature"
                        :label="feature" 
                        :checked="selectedFeatures.includes(feature)"
                        @click="$emit('toggleFeature', feature)"
                    />
                </div>

                <p class="label"
                    v-if="additionalFeatures.length > 0"
                >Other Features</p>
                <div class="card-features">
                    <SelectableTag 
                        v-if="additionalFeatures.length > 0"
                        v-for="feature in additionalFeatures" 
                        :key="feature"
                        :label="feature" 
                        :checked="selectedFeatures.includes(feature)"
                        @click="$emit('toggleFeature', feature)"
                    />
                </div>
            </div>

            <div class="card-footer">
                <div class="card-spacer">
                    <p class="price">£{{ Number(price).toFixed(2) }}</p>
                    <AppButton 
                        text="Save" 
                        leftIcon="folder_open"
                        theme="secondary"
                        :disabled="saved || !loggedIn"
                        @click="saveProduct"
                    />
                </div>
                <LinkButton 
                    text="Go to website"
                    :href="webUrl"
                    leftIcon="open_in_new"
                    :fullWidth="true"
                    theme="tertiary"
                />
            </div>
        </div>
    </article>
</template>

<script>
import AppButton from '../elements/AppButton.vue'
import LinkButton from '../elements/LinkButton.vue'
import SelectableTag from '../elements/SelectableTag.vue'
import { useAccountStore } from '@/stores/accountStore.js';
import { addProduct } from '@/services/databaseService.js'

export default {
  name: "ProductCard",
  props: {
    name: {
      type: String,
      default: "Product Name",
    },
    brand: {
        type: String,
        default: "Brand Name"
    },
    rating: {
        type: Number,
        default: 0.0
    },
    image: {
      type: String,
      default: "",
    },
    features: {
      type: Array,
      default: () => []
    },
    additionalFeatures: {
      type: Array,
      default: () => []
    },
    price: {
      type: Number,
      default: 0,
    },
    webUrl: {
      type: String,
      default: "",
    },
    selectedFeatures: {
      type: Array,
      default: () => [],
    },
    tag: {
        type: String,
        default: "",
    }
  },
  components: {
    AppButton,
    LinkButton,
    SelectableTag,
  },
  data() {
    return {
        accountStore: useAccountStore(),
        saved: false,
        loggedIn: false,
    }
  },
  mounted() {
    this.loggedIn = this.accountStore.isLoggedIn
  },
  methods: {
    async saveProduct(){
        try {
            await addProduct(
                this.accountStore.email,
                this.accountStore.password,
                {
                    "name": this.name,
                    "brand": this.brand,
                    "rating": this.rating,
                    "image": this.image,
                    "webUrl": this.webUrl,
                    "price": this.price,
                    "tag": this.tag,
                }
            )
            this.saved = true
            alert('Saved')
        } catch (error) {
            console.error('Failed to save product:', error)
            alert('Could not save product')
            return false
        }
    }
  }
};
</script>

<style scoped>
.product-card {
    width: 100%;
    height: 70vh;
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: var(--gap);
    font-size: 2rem;
    background: var(--card-background);
    border: 1px solid var(--border);
    border-radius: var(--border-radius);
    box-shadow: var(--shadow-small);
    overflow: hidden;
}

.card-main-and-footer {
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: var(--gap);
    font-size: 2rem;
}

.card-title {
    font-size: 1.2rem;
    font-family: var(--font-secondary);
    font-weight: 600;
    margin: 0;
}

.card-image {
    width: 100%;
    height: 30vh;
    position: relative;
    overflow: clip;
}

.card-image img {
    object-fit: contain;
    width: 100%;
    height: 100%;
}

.card-main {
    display: flex;
    flex-direction: column;    
    padding: var(--padding-large);
    gap: var(--gap);
    overflow: hidden;
    overflow-y: auto;
    max-height: 44vh;
}

.card-features {
    display: flex;
    flex-wrap: wrap;
    gap: var(--gap);
    margin-bottom: var(--gap);
}

.card-spacer {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.card-footer {
    border-top: 2px solid var(--half-rule);
    padding: var(--padding-large);
    padding-top: var(--padding);
    flex-direction: column;
    margin-top: auto;
    gap: var(--gap);
    display: flex;
}

.card-details {
    color: var(--grey-text);
    display: flex;
    align-items: center;
    justify-content: start;
    gap: 5px;
}
.card-details * {
    font-size: 0.85rem;
}
.card-details hr {
    height: 100%;
    background-color: var(--border);
    border-color:  var(--border);
}

.card-rating {
    color: var(--main-text);
}

.card-star {
    color: var(--yellow-icon);
    font-variation-settings:
    'FILL' 1;
}

.label {
    font-size: 0.8rem;
}

.price {
    color: var(--primary);
}

.card-tag {
    background-color: var(--primary);
    color: white;
    position: absolute;
    top: var(--padding-large);
    right: var(--padding-large);
    padding: var(--padding) var(--padding-large);
    border-radius: var(--border-radius);
    gap: var(--gap);
    display: inline-flex;
    justify-content: center;
    align-items: center;
}

.card-tag__icon {
    color: inherit;
}

.saved-product-card {
    height: min-content;
    width: 50vw;
    flex-direction: row;
    flex-shrink: 0;
}
.saved-product-card .card-main{
    overflow-y: hidden;
}
.saved-product-card .card-image{
    height: 20vh;
    width: 20vw;
}
.saved-product-card .secondary {
    display: none;
}
</style>