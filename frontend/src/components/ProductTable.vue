<template>
    <table class="product-table">
      <thead>
        <tr>
          <th class="table-header"></th>
          <th v-for="product in products" :key="product.name">
            <div class="table-product-preview">
                <div class="table-image">
                    <img :src="product.image" :alt="`Image of ${product.name}`" />
                </div>
                <div class="table-essentials">
                    <span class="table-tag">
                        <span class="button-icon material-symbols-outlined table-star table-tag__icon"> star </span>
                        Best Fit
                    </span>
                    <span class="table-title">{{ product.name }}</span>
                    <p class="price">£{{ Number(product.price).toFixed(2) }}</p>
                </div>
            </div>
          </th>
        </tr>
      </thead>

      <tbody>
        <tr>
          <td class="table-header"> Brand </td>

          <td v-for="product in products" :key="product.name">
            {{product.brand}}
          </td>
        </tr>
        <tr v-for="row in 6" :key="row.label">
          <td class="table-header"> Feature Name </td>

          <td v-for="product in products" :key="product.name">
            Feature Name
          </td>
        </tr>
        <tr>
          <td class="table-header">Rating</td>

          <td v-for="product in products" :key="product.name">
                <div class="table-rating">
                    <span> {{product.rating}} </span>
                    <span class="button-icon material-symbols-outlined table-star"> star </span>
                    <span
                        v-for="star in 5"
                        :key="star"
                        class="material-symbols-outlined table-star"
                    >
                        {{ getStarIcon(star, product.rating) }}
                    </span>
                </div>
          </td>
        </tr>
        <tr>
          <td class="table-header">View Product</td>

          <td v-for="product in products" :key="product.name">
                <LinkButton 
                    text="Go to website"
                    :href="product.webUrl"
                    leftIcon="open_in_new"
                    :fullWidth="true"
                    theme="tertiary"
                />
          </td>
        </tr>
      </tbody>
    </table>
</template>

<script>
import AppButton from '../elements/AppButton.vue'
import LinkButton from '../elements/LinkButton.vue'
import SelectableTag from '../elements/SelectableTag.vue'

export default {
  name: "ProductCard",
  props: {
    products: {
      type: Array,
      default: () => []
    },
  },
  components: {
    AppButton,
    LinkButton,
    SelectableTag,
  },
  methods: {
    getStarIcon(starPosition, rating) {
        if (rating >= starPosition) {
        return 'star'
        }

        if (rating >= starPosition - 0.5) {
        return 'star_half'
        }

        return 'star_outline'
    }
  }
};
</script>

<style scoped>
.product-table {
    border-collapse: collapse;
    width: 100%;
    height: 70vh;
    position: relative;
    font-size: 2rem;
    background: var(--card-background);
    border-color: var(--table-border);
    box-shadow: var(--shadow-small);
    overflow: hidden;
}

.table-title {
    font-size: 1.2rem;
    font-family: var(--font-secondary);
    font-weight: 600;
    margin: 0;
}

.table-image {
    width: 150px;
    height: 150px;
    background: var(--light);
    padding: calc(var(--padding) / 2);
    position: relative;
    overflow: clip;
}

.table-image img {
    object-fit: contain;
    width: 100%;
    height: 100%;
}

.table-rating {
    color: var(--main-text);
    gap: var(--gap);
    display: inline-flex;
    align-items: center;
}

.table-star {
    color: var(--yellow-icon);
    font-variation-settings:
    'FILL' 1;
}

.price {
    color: var(--primary);
    margin-top: auto;
}

.table-tag {
    background-color: var(--primary);
    color: white;
    padding: var(--padding) var(--padding-large);
    border-radius: var(--border-radius);
    gap: var(--gap);
    display: inline-flex;
    justify-content: center;
    align-items: center;
}

.table-tag__icon {
    color: inherit;
}

.table-product-preview {
    display: flex;
    gap: var(--gap);
}

.table-essentials {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: var(--gap);
    padding: var(--padding);
    text-align: left;
}

.table-header {
    background-color: var(--light);
    width: 150px;
    padding: var(--padding);
}

td,
th {
    border: 1px solid var(--table-border);
    padding: var(--padding-large);
}
</style>