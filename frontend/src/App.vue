<script setup>
import AppButton from './elements/AppButton.vue'
import RangeSlider from './elements/RangeSlider.vue'
import SelectableImage from './elements/SelectableImage.vue'
import SelectableTag from './elements/SelectableTag.vue'
import SuggestionInput from './components/SuggestionInput.vue'
import BudgetSelect from './components/BudgetSelect.vue'
import ProductCard from './components/ProductCard.vue'
</script>

<template>
  <header>
    <img alt="Vue logo" class="logo" src="./assets/logo.svg" width="125" height="125" />
  </header>

    <AppButton text="Click me" icon="add" />
    <RangeSlider :min="25" :max="75" />
    <SelectableImage image="https://picsum.photos/200/300" />
    <SelectableTag label="Tag" />
    <SuggestionInput
      :suggestions="[
        'Headphones...',
        'Bed Frames...',
        'Running Shoes...',
        'Coffee Makers...',
        'Desk Lamps...',
        'Yoga Mats...'
      ]"
    />
    <BudgetSelect />
    <ProductCard 
      name="Product Name" 
      image="https://picsum.photos/200/300" 
      :features="['Feature 1', 'Feature 2', 'Feature 3']" 
      :additionalFeatures="['Feature 1', 'Feature 2', 'Feature 3']" 
      price="999.99"
    />
</template>

<style scoped>
</style>
