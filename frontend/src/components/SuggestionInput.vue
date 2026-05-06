<template>
    <form class="search-box">
        <input 
        `   type="text"
            :placeholder="placeholder"
            name="product" 
            required 
            minlength="2"
        />
        <AppButton type="submit" icon="search" />
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
        },
    }
</script>

<style scoped>
.search-box {
    display: flex;
    width: 100%;
    background: var(--light-green);
    padding: 5px;
}

.search-box:has(input:focus-visible) {
    outline: -webkit-focus-ring-color auto 5px;
}

.search-box input {
    width: 100%;
    background: none;
    border: 0;
    outline: none;
    box-shadow: none;
}
</style>