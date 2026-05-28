<template>
    <button
      @click="click"
      :type="type"
      :disabled="disabled"
      :class="[theme, { 'full-width': fullWidth }]"
    >
        <span 
          v-if="leftIcon"
          class="button-icon material-symbols-outlined"> 
          {{leftIcon}}
        </span>
        <span
          v-if="text"> 
          {{text}} 
        </span>
        <span 
          v-if="rightIcon"
          class="button-icon material-symbols-outlined"> 
          {{rightIcon}}
        </span>
    </button>
</template>

<script>
export default {
  props: {
    text: String,
    leftIcon: String,
    rightIcon: String,
    theme: {
      type: String,
      default: "primary"
    },
    type: {
      type: String,
      default: "button"
    },
    disabled: {
      type: Boolean,
      default: false,
    },
    fullWidth: {
      type: Boolean,
      default: false,
    }
  },
  methods: {
    click() {
      if (!this.disabled) {
        this.$emit("click");
      }
    }
  }
}
</script>

<style scoped>
button {
  padding: var(--padding-large) calc(var(--padding-large) * 2);
  border-radius: var(--border-radius);
  border: 0;
  margin: 0;
  gap: var(--gap);
  cursor: pointer;
  width: fit-content;
  height: fit-content;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  transition: background 0.2s ease;
}

.primary {
  background-color: var(--primary);
  color: var(--white);
}
.primary:hover,
.primary:focus-visible {
  background: var(--primary-hover);
}

.secondary {
  background-color: var(--light);
  color: var(--primary);
}
.secondary:hover,
.secondary:focus-visible {
  background: var(--light-hover);
}

.tertiary {
  background-color: var(--card-background);
  border: 2px solid var(--primary);
  color: var(--primary);
}
.tertiary:hover,
.tertiary:focus-visible {
  background: var(--card-hover);
}

.ghost {
  background: transparent;
  color: var(--main-text)
}
.ghost:hover,
.ghost:focus-visible {
  background: var(--light-hover);
  color: var(--primary);
}

.full-width {
  width: 100%;
}

button:focus-visible {
  outline: 5px solid var(--outline);
  outline-offset: 3px;
}

button:disabled,
button:disabled:hover {
  background: var(--disabled);
  color: var(--grey-text);
  cursor: not-allowed;
}
</style>