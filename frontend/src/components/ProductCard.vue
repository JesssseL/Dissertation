<template>
    <article class="product-card">
        <div class="card-image">
            <img :src="image" :alt="`Image of ${name}`" />
        </div>

        <div class="card-main">
            <h2 class="card-title"> {{name}} </h2>
            <div class="card-details"> 
                <span class="button-icon material-symbols-outlined"> sell </span>
                <span> {{brand}} </span>
                <hr/>
                <span class="button-icon material-symbols-outlined card-star"> star </span>
                <span class="card-rating"> {{rating}} </span>
            </div>

            <p class="label">Reccomended Features</p>
            <div class="card-features">
                <SelectableTag 
                    v-for="feature in features" 
                    :key="feature"
                    :label="feature" 
                    :checked="selectedFeatures.includes(feature)"
                    @click="$emit('toggleFeature', feature)"
                />
            </div>

            <p class="label">Other Features</p>
            <div class="card-features">
                <SelectableTag 
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
    </article>
</template>

<script>
import AppButton from '../elements/AppButton.vue'
import LinkButton from '../elements/LinkButton.vue'
import SelectableTag from '../elements/SelectableTag.vue'

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
  },
  components: {
    AppButton,
    LinkButton,
    SelectableTag,
  },
};
</script>

<style scoped>
.product-card {
    width: 100%;
    height: 100%;
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

.card-title {
    font-size: 1.2rem;
    font-family: var(--font-secondary);
    font-weight: 600;
    margin: 0;
}

.card-image {
    width: 100%;
    height: 175px;
    position: relative;
    overflow: clip;
}

.card-image img {
    object-fit: cover;
    width: 100%;
    height: 100%;
}

.card-main {
    display: flex;
    flex-direction: column;    
    padding: var(--padding-large);
    gap: var(--gap);
    overflow: hidden;
    overflow-y: scroll;
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
</style>