<template>
    <div 
        v-if="showPannel && open" 
        class="pannel"
        ref="aiPannel"
    >
        <div class="pannel-close">
            <span class="pannel-title"> 
                Ask Ai
            </span>
            <AppButton
                leftIcon="close"
                theme="tertiary"
                @click="closeMenu"
            />
        </div>

        <div class="pannel-main">
            <AiMessage 
                v-for="message in messages"
                :sender="message.sender"
                :text="message.text"
            />
        </div>

        <AiSuggestion 
            :suggestedSearchTerm="suggestedSearchTerm"
            @newSearch="updateSearch"    
        />

        <div class="pannel-user-area">
            <label class="pannel-user-label">
                Ask anything
            </label>
            <SuggestionInput 
                :suggestions="[
                'What features should I look for?',
                'Which option is best for work?',
                'Explain the technical terms',
                'Which product has the best value?',
                'Help me refine my search'
                ]"
                :buttonDisabled="messageSending"
                :buttonText="''"
                buttonIcon="send"
                @search="sendMessage"
            />
            <span class="pannel-warning">
                <span class="material-symbols-outlined">warning</span>
                AI can make mistakes, double check important information
            </span>
        </div>
    </div>
    <AppButton
        v-if="showPannel && !open"
        class="pannel-button"
        leftIcon="wand_stars"
        theme="tertiary"
        @click="openMenu"
    />
</template>

<script>
import AiMessage from '@/elements/AiMessage.vue';
import AiSuggestion from '@/elements/AiSuggestion.vue'
import AppButton from '@/elements/AppButton.vue';
import SuggestionInput from './SuggestionInput.vue';
import { useSearchStore } from '@/stores/searchStore'
import { useAiStore } from '@/stores/aiStore';

export default {
  name: "AiPannel",
  props: {
    currentRoute: {
        type: String,
        required: true
    }
  },
  components: {
    AiMessage,
    AiSuggestion,
    AppButton,
    SuggestionInput
  },
  data() {
    return {
        searchStore: useSearchStore(),
        aiStore: useAiStore(),
        open: false,
    }
  },
  computed: {
    messages() {
        return this.aiStore.messages
    },
    messageSending() {
        return this.aiStore.messageSending
    },
    showPannel() {
        if (
            this.currentRoute === 'Home' ||
            this.currentRoute === 'Budget' ||
            this.currentRoute === 'Results'
        ) {
            return true
        } else {
            return false
        }
    }
  },
  mounted() {
    document.addEventListener('click', this.handleOutsideClick, true)
  },
  beforeUnmount() {
    document.removeEventListener('click', this.handleOutsideClick, true)
  },
  methods: {
    openMenu() {
        this.open = true
    },
    closeMenu() {
        this.open = false
    },
    handleOutsideClick(event) {
        if (!this.open) return

        const menu = this.$refs.aiPannel
        if (menu && !menu.contains(event.target)) {
            this.closeMenu()
        }
    },
    updateSearch(event) {
      this.searchStore.setQuery(event)
      if (this.currentRoute == "Home") {
        this.$router.push('/intent')
      }
    },
    async sendMessage(event) {
        this.aiStore.sendUserMessage(event)
        // API call to get response
        this.aiStore.sendAIMessage(
            'These Sony headphones are strong for office use because they have excellent microphone quality and active noise cancellation...'
        )
    }
  },
};
</script>

<style scoped>
.pannel-button {
    position: absolute;
    right: var(--padding-large);
    top: var(--padding-large);
}
.pannel {
    position: absolute;
    right: 0;
    top: 0;
    width: 60%;
    height: 100%;
    display: flex;
    flex-direction: column;
    gap: var(--gap);
    background: var(--background-gradient);
    border: 1px solid var(--border);
    border-radius: var(--border-radius);
    box-shadow: var(--shadow-small);
}
.pannel > * {
    
    padding: var(--padding-large);
}
.pannel-close {
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.pannel-warning {
    display: inline-flex;
    align-items: center;
    gap: var(--gap);
    color: var(--grey-text);
    font-size: 0.8rem;
}
.pannel-title {
    font-family: var(--font-secondary);
    font-size: 2rem;
    font-weight: 600;
    line-height: 1;
    letter-spacing: 0.02em;
}
.pannel-user-area { 
    display: flex;
    flex-direction: column;
    display: flex;
    flex-direction: column;
    gap: var(--padding-large);
    padding: var(--padding-large);
    background: var(--background-gradient);
    border: 1px solid var(--border);
    border-top: 2px solid var(--half-rule);
}
.pannel-user-label,
.pannel-search-suggestion p {
    font-family: var(--font-secondary);
    font-size: 1.2rem;
    font-weight: 600;
    line-height: 1;
    letter-spacing: 0.02em;
}
.pannel-main {
    display: flex;
    flex-direction: column;
    gap: var(--gap);
    overflow-y: auto;
    margin-top: auto;
}
.pannel-search-suggestion {
    display: flex;
    justify-content: space-between;
    margin: var(--padding-large);
    border-radius: var(--border-radius);
    border: 2px solid var(--secondary);
    color: var(--primary);
}
.pannel-search-suggestion-text {
    display: flex;
    flex-direction: column;
    gap: var(--gap)
}
</style>