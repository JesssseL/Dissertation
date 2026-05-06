<script setup>
import AppButton from './elements/AppButton.vue'
import RangeSlider from './elements/RangeSlider.vue'
import SelectableImage from './elements/SelectableImage.vue'
import SelectableTag from './elements/SelectableTag.vue'
import SuggestionInput from './components/SuggestionInput.vue'
import BudgetSelect from './components/BudgetSelect.vue'
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
</template>

<style scoped></style>
