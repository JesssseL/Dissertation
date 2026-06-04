<template>
    <div 
        v-if="suggestedSearchTerm" 
        class="suggestion"
    >
        <div class="suggestion-text">
            <span class="suggestion-label">Suggested search</span>
            <div
                class="suggestion-edit" 
                v-if="editing"
            >
                <input
                    v-model="userSearchTerm"
                    class="suggestion-input"
                    @keyup.enter="finishEdit"
                    @keyup.esc="cancelEdit"
                    autofocus
                />
                <div class="suggestion-buttons">
                    <AppButton
                        rightIcon="close"
                        theme="primary"
                        @click="cancelEdit"
                    />
                    <AppButton 
                        rightIcon="check"
                        theme="primary"
                        @click="finishEdit"
                    />
                </div>
            </div>
            <p class="suggestion-main" v-else>
                {{ searchTerm }}             
                <button 
                    class="material-symbols-outlined edit-button"
                    @click="startEdit"
                >
                    edit
                </button>
            </p>
        </div>

        <AppButton
            v-if="!editing"
            text="Update search"
            rightIcon="search"
            theme="primary"
            @click="updateSearchQuery"
        />
    </div>
</template>

<script>
import AppButton from '@/elements/AppButton.vue';

export default {
  name: "AiSuggestion",
  props: {
    suggestedSearchTerm: {
        type: String,
        required: true
    }
  },
  components: {
    AppButton,
  },
  data() {
    return {
        editing: false,
        userSearchTerm: '',
        savedSearchTerm: ''
    }
  },
  computed: {
    searchTerm() {
        return this.savedSearchTerm.trim()
            ? this.savedSearchTerm
            : this.suggestedSearchTerm
    }
  },
  methods: {
    startEdit() {
        this.userSearchTerm = this.searchTerm
        this.editing = true
    },
    finishEdit() {
        this.editing = false
        this.savedSearchTerm = this.userSearchTerm
    },
    cancelEdit() {
        this.editing = false
        this.userSearchTerm = this.savedSearchTerm
    },
    updateSearchQuery() {
    console.log('AiSuggestion emit')
        this.$emit('newSearch', this.searchTerm)
        this.savedSearchTerm = ''
    },
  }
}
</script>

<style scoped>
p {
    font-family: var(--font-secondary);
    font-size: 1.6rem;
    font-weight: 600;
    line-height: 1;
    letter-spacing: 0.02em;
}
.suggestion {
    display: flex;
    justify-content: space-between;
    margin: var(--padding-large);
    border-radius: var(--border-radius);
    border: 2px solid var(--secondary);
    color: var(--primary);
}
.suggestion-text {
    display: flex;
    flex-direction: column;
    gap: var(--gap);
    width: 100%;
}
.suggestion-label {
    font-size: 0.75rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
}
.edit-button {
    background: transparent;
    border: none;
    font-size: inherit;
    color: inherit
}
.edit-button:hover,
.edit-button:focus-visible {
    background: var(--light);
    color: var(--main-text)
}
.suggestion-edit {
    gap: var(--gap);
    display: flex;
    width: 100%;
}
.suggestion-buttons {
    display: flex;
    flex-direction: column;
    gap: var(--gap);
    width: min-content;
}
input {    
    width: 100%;
    border: 1px solid var(--secondary);
    border-radius: var(--border-radius);
    padding: var(--padding-large);
    font-family: var(--font-secondary);
    font-size: 1.4rem;
    font-weight: 600;
    color: var(--primary);
    background: var(--white);
    outline: none;
}
button {    
    text-wrap: nowrap;
    align-self: center;
}
</style>