<template>
    <div class="feature_view container">
        <div class="header">
          <h1> Tell us what matters </h1>
          <h2> Select all that apply </h2>
        </div>

        <div class="feature_container">
            <SelectableTag 
                v-for="feature in discoveryFeatures"
                :key="feature"
                :label="feature"
            />
        </div>

        <AppButton 
          text="Next"
          :disabled="searchFeatures == []"
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
    this.searchFeatures = [...this.searchStore.features]
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
button {
  align-self: flex-end;
}
</style>