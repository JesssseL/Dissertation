<script setup>
import AppButton from './elements/AppButton.vue'
import RangeSlider from './elements/RangeSlider.vue'
import SelectableImage from './elements/SelectableImage.vue'
import SelectableTag from './elements/SelectableTag.vue'
import SuggestionInput from './components/SuggestionInput.vue'
</script>

<template>
  <header>
    <img alt="Vue logo" class="logo" src="./assets/logo.svg" width="125" height="125" />
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
  </header>
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
