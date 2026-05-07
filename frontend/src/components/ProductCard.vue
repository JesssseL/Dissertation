<template>
    <article class="product-card">
        <div class="card-image">
            <img :src="image" :alt="`Image of ${name}`" />
        </div>

        <div class="card-main">
            <h2 class="card-title"> {{name}} </h2>

            <p class="label">Features</p>
            <div class="card-features">
                <SelectableTag 
                    v-for="feature in features" 
                    :key="feature"
                    :label="feature" 
                    :checked="true" 
                />
            </div>

            <p class="label">Additional Features</p>
            <div class="card-features">
                <SelectableTag 
                    v-for="feature in additionalFeatures" 
                    :key="feature"
                    :label="feature" 
                    :checked="false" 
                />
            </div>
        </div>

        <div class="card-footer">
            <div class="card-spacer">
                <p class="price">£999.99</p>
                <AppButton 
                    text="Save" 
                    leftIcon="folder_open"
                    theme="secondary"
                />
            </div>
            <AppButton 
                text="Go to website" 
                leftIcon="open_in_new"
                :fullWidth="true"
                theme="tertiary"
            />
        </div>
    </article>
</template>

<script>
import AppButton from '../elements/AppButton.vue'
import SelectableTag from '../elements/SelectableTag.vue'

export default {
  name: "ProductCard",
  props: {
    name: {
      type: Number,
      default: 0,
    },
    image: {
      type: String,
      default: "",
    },
    features: {
      type: Array,
      default: [],
    },
    additionalFeatures: {
      type: Array,
      default: [],
    },
    price: {
      type: Number,
      default: 0,
    },
  },
  components: {
    AppButton,
    SelectableTag,
  },
};
</script>

<style scoped>
.product-card {
    padding: var(--padding-large);
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
    border-radius: var(--border-radius);
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
    gap: var(--gap);
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
    border-top: 2px solid black;
    padding-top: var(--padding);
    flex-direction: column;
    margin-top: auto;
    gap: var(--gap);
    display: flex;
}

.label {
    font-size: 0.8rem;
}

.price {
    color: var(--primary);
}
</style>