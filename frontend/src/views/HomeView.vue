<template>
    <div class="home container">
        <h1 class="header">What are you <br/> shopping for <span class="accent">today</span>?</h1>
        <SuggestionInput
            :suggestions="[
            'Headphones...',
            'Bed Frames...',
            'Running Shoes...',
            'Coffee Makers...',
            'Desk Lamps...',
            'Yoga Mats...'
            ]"
            @search="search"
        />
    </div>
</template>

<script>
import SuggestionInput from '../components/SuggestionInput.vue'
import { useSearchStore } from '../stores/searchStore'
import { useAiStore } from '@/stores/aiStore';

export default {
  name: "HomeView",
  components: {
    SuggestionInput,
  },
  data() {
    return {
      searchStore: useSearchStore(),
      aiStore: useAiStore(),
    };
  },
  methods: {
    search(event) {
      this.searchStore.setQuery(event)
      this.aiStore.sendStatusMessage('user', `Search Query set to: ${event}`)
      this.$router.push('/intent')
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

.home {
  width: 60%;
  max-width: 900px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

@media (max-width: 1000px) {
  .home {
    width: 80%;
  }
}
</style>