<template>
    <section class="container loading-page">
    
    <div class="loading-content">

      <span class="material-symbols-outlined loading-icon">
        shopping_bag
      </span>

      <h1 class="loading-text">
        Finding the best
        <span class="accent">[x]</span>
        for you
      </h1>

      <p>Please wait while we personalise your recommendations.</p>

    </div>

    </section>
</template>

<script>
import SuggestionInput from '../components/SuggestionInput.vue'
import { useSearchStore } from '../stores/searchStore'

export default {
  name: "HomeView",
  components: {
    SuggestionInput,
  },
  methods: {
    search(event) {
      const searchStore = useSearchStore()
      searchStore.setQuery(event)
    },
  },
};
</script>

<style scoped>
h1,
h1 * {
  font-family: var(--font-secondary);
  font-size: 4rem;
  font-weight: 400;
  line-height: 1;
  letter-spacing: -0.02em;
  text-align: center;
  display: inline;
}

.loading-page {
  display: flex;
  align-items: center;
  justify-content: center;
}

.loading-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: 1rem;
}

.loading-text {
    max-width: 600px;
}

p {
    color: var(--grey-text);
}

.loading-icon {
  font-size: 7rem;
  color: var(--primary);
  animation: spin 1.5s linear infinite;
}

@keyframes spin {
  from {
    transform: rotate(0deg);
  }

  to {
    transform: rotate(360deg);
  }
}
</style>