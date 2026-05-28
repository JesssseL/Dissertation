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
        open: false,
        messageSending: false,
        suggestedSearchTerm: '',
        messages: [
            {
                sender: 'ai',
                text: 'I analysed your search for wireless headphones and found a few strong options for work and calls.'
            }
        ]
    }
  },
  watch: {},
  computed: {
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
        this.messages.push({
            sender: 'user',
            text: event
        })

        // fake ai response
        await this.newAIMessage(
            'These Sony headphones are strong for office use because they have excellent microphone quality and active noise cancellation.'
        )
    },
    async newAIMessage(message) {
        this.messages.push({
            sender: 'ai',
            text: ''
        })
        this.messageSending = true
        const messageIndex = this.messages.length - 1

        for (let i = 0; i < message.length; i++) {
            const currentText = this.messages[messageIndex].text + message[i]
            this.messages.splice(messageIndex, 1, {
                sender: 'ai',
                text: currentText
            })
            await new Promise(resolve => setTimeout(resolve, 25))
        }
        this.suggestedSearchTerm = 'Noise cancelling headphones for work'
        this.messageSending = false
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