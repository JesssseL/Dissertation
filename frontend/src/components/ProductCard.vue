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

            <div class="card-footer">
                <p>£999.99</p>
                <AppButton text="Save" icon="folder" />
            </div>
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
    width: 300px;
    height: fit-content;
    background-color: whitesmoke;
}

.card-title {
    font-size: large;
    text-align: center;
    margin: 0;
}

.card-image {
    width: 100%;
    height: 200px;
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
    padding: 10px;
    gap: 5px;
}

.card-features {
    display: flex;
    flex-wrap: wrap;
    gap: 5px;
}

.card-footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 2px solid black;
    padding-top: 5px;
}
</style>