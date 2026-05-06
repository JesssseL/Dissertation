<template>
    <button
      @click="click">
        <span 
          v-if="icon"
          class="button-icon material-symbols-outlined"> 
          {{icon}}
        </span>
        <span
          v-if="text"> 
          {{text}} 
        </span>
    </button>
</template>

<script>
export default {
  props: {
    text: String,
    icon: String,
  },
  methods: {
    click() {
      this.$emit("click");
    }
  }
}
</script>

<style scoped>
button {
  background-color: var(--green);
  color: white;
  padding: 5px 10px;
  border-radius: 5px;
  border: 0;
  margin: 0;
}
button:hover {
  background-color: red;
}

.button-icon {
  margin-right: 5px;
}
</style>