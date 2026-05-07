<template>
    <form class="search-box" @submit.prevent="submitSearch">
        <input 
            type="text"
            :placeholder="placeholder"
            name="product" 
            required 
            minlength="2"
            v-model="inputText"
        />
        <AppButton 
            text="Search" 
            type="submit" 
            leftIcon="search"
            @submit.prevent="submitSearch"
        />
    </form>
</template>

<script>
import AppButton from '../elements/AppButton.vue'

export default {
    name: "SuggestionInput",
    props: {
        suggestions: {
            type: Array,
            default: () => [],
        },
    },
    components: {
        AppButton,
    },
    data() {
        return {
            arrayIndex: 0,
            characterIndex: 0,
            typingSpeed: 150,
            placeholder: "",
            timer: null,
            inputText: "",
        };
    },
    mounted() {
        this.typeEffect();
    },
    beforeUnmount() {
        clearTimeout(this.timer);
    },
    methods: {
        typeEffect() {
            if (this.suggestions.length === 0) return;

            const currentText = this.suggestions[this.arrayIndex];
            this.characterIndex++;
            this.placeholder = currentText.substring(0, this.characterIndex);
            this.typingSpeed = 200;

            if (this.characterIndex === currentText.length) {
                this.arrayIndex = (this.arrayIndex + 1) % this.suggestions.length;
                this.characterIndex = 0;
                this.typingSpeed = 1000;
            }

            this.timer = setTimeout(this.typeEffect, this.typingSpeed);
        },
        submitSearch() {
            this.$emit("search", this.inputText); 
        }
    },
}
</script>

<style scoped>
.search-box {
    display: flex;
    width: 100%;
    background: var(--card-background);
    border: 1px solid var(--border);
    border-radius: var(--border-radius);
    box-shadow: var(--shadow);
    padding: var(--padding);
    padding-left: var(--padding-large);
}

.search-box:has(input:focus-visible) {
    outline: var(--outline) auto 5px;
}

.search-box input {
    width: 100%;
    background: none;
    border: 0;
    outline: none;
    box-shadow: none;
}

.search-box input::placeholder {
  color: rgba(21, 21, 21, 0.35);
}
</style>