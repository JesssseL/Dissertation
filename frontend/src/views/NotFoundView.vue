<template>
    <div class="not-found container">
        <h1 class="header"> <span class="accent">404</span> <br/> Page not found</h1>

        <p>
            The page you are looking for does not exist.
        </p>

        <AppButton
            text="Return to search"
            leftIcon="search"
            @click="returnToSearch"
        />
    </div>
</template>

<script>
import AppButton from '@/elements/AppButton.vue'

export default {
  name: "NotFound",
  components: {
    AppButton,
  },
  methods: {
    returnToSearch() {
      this.$router.push('/')
    }
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

.not-found {
  width: 60%;
  max-width: 900px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 20px
}

@media (max-width: 1000px) {
  .not-found {
    width: 80%;
  }
}
</style>