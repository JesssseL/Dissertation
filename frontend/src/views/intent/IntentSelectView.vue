<template>
    <div class="intent-buttons container">
        <AppButton
            text="Questions"
            @click="useQuestions"
        />
        <AppButton
            text="Photos"
            @click="usePhotos"
        />
        <AppButton
            text="Features"
            @click="useFeatures"
        />
    </div>
</template>

<script>
import AppButton from '@/elements/AppButton.vue'
import { useDiscoveryStore } from '@/stores/discoveryStore';
export default {
  name: "Intent",
  components: {
    AppButton,
  },
  data() {
    return {
      discoveryStore: useDiscoveryStore(),
    }
  },
  methods: {
    useQuestions() {
      this.discoveryStore.intentStyle = "Questions"
      this.loadNextStage()
    },
    usePhotos() {
      this.discoveryStore.intentStyle = "Photos"
      this.loadNextStage()
    },
    useFeatures() {
      this.discoveryStore.intentStyle = "Features"
      this.loadNextStage()
    },
    loadNextStage() {
      this.$router.push('/loading/intent')
    }
  },
};
</script>

<style scoped>
.intent-buttons {
  width: 60%;
  max-width: 900px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 20px
}

@media (max-width: 1000px) {
  .intent-buttons {
    width: 80%;
    flex-direction: column;
  }
}
</style>