<template>
    <div class="feature_view container">
        <div class="header">
          <h1> Tell us what matters </h1>
          <h2> Select all that apply </h2>
        </div>

        <div class="feature_stage">
          <div class="query_card">
            <h3 class="header-style">{{ searchStore.query }}</h3>
          </div>

          <div class="feature_container">
            <SelectableTag 
              v-for="feature in discoveryFeatures"
              :key="feature"
              :label="feature"
              @click="addSearchFeature(feature)"
            />
          </div>
        </div>

        <AppButton 
          text="Next"
          :disabled="searchFeatures.length === 0"
          rightIcon="arrow_forward"
          @click="saveFeatures"
        />
    </div>
</template>

<script>
import AppButton from '@/elements/AppButton.vue'
import SelectableTag from '@/elements/SelectableTag.vue';
import { useSearchStore } from '../../stores/searchStore'
import { useDiscoveryStore } from '../../stores/discoveryStore'

export default {
  name: "FeatureView",
  components: {
    AppButton,
    SelectableTag
  },
  data() {
    return {
      searchStore: useSearchStore(),
      discoveryStore: useDiscoveryStore(),
      discoveryFeatures: [],
      searchFeatures: [],
    }
  },
  mounted() {
    this.discoveryFeatures = [...this.discoveryStore.commonFeatures]
  },
  methods: {
    addSearchFeature(feature) {
      if (this.searchFeatures.includes(feature)) {
        this.searchStore.removeFeature(feature)
      }
      else {
        this.searchStore.addFeature(feature)
      }
      this.searchFeatures = this.searchStore.features
    },
    saveFeatures() {
      this.$router.push('/budget')
    }
  },
};
</script>

<style scoped>
.feature_view {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.feature_container {
  max-width: 900px;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: calc(var(--gap) * 2);
}

button {
  margin-top: auto;
  align-self: flex-end;
}

.feature_stage {
  flex: 1;
  display: grid;
  place-items: center;
  gap: 2.5rem;
  align-content: center;
}

.query_card {
  text-align: center;
}

h3 {
  font-size: clamp(2rem, 5vw, 4rem);
}
</style>