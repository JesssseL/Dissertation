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
            <div
                v-if="messageLoading" 
                class="pannel_message_loading"
            >
                <span class="pannel_message_loading-dot"></span>
                <span class="pannel_message_loading-dot"></span>
                <span class="pannel_message_loading-dot"></span>
            </div>
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
        messageLoading: false,
        aiStore: useAiStore(),
        open: false,
    }
  },
  computed: {
    messages() {
        return this.aiStore.messages
    },
    messageSending() {
        return this.messageLoading && this.aiStore.messageSending
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
        this.messageLoading = true
        const aiResponse = await this.getAIMessageResponse(event)
        this.messageLoading = false
        this.aiStore.sendAIMessage(aiResponse)
    },
    async getAIMessageResponse(userMessage) {
        let aiResponse = userMessage
                            .split('')
                            .sort(() => Math.random() - 0.5)
                            .join('')
        if (aiResponse == '') {
            return 'Response could not be generated'
        }
        return aiResponse
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

.pannel_message_loading {
    border-radius: var(--border-radius);
    padding: var(--padding-large);
    width: fit-content;
    max-width: 80%;
    word-break: break-word;
    align-self: flex-end;
    color: var(--main-text);
    padding: var(--padding-large);
    border: 1px solid var(--border);
    border-radius: var(--border-radius);
    box-shadow: var(--shadow-small);
    background-color: white;
    align-self: flex-start;
    display: inline-flex;
    gap: var(--gap)
}
.pannel_message_loading-dot {
    display: block;
    width: 0.5rem;
    height: 0.5rem;
    border-radius: 50%;
    background-color: var(--primary);
    animation: loading-dot 1.4s infinite ease-in-out;
}
.pannel_message_loading-dot:nth-child(2) {
    animation-delay: 0.2s;
}
.pannel_message_loading-dot:nth-child(3) {
    animation-delay: 0.4s;
}

@keyframes loading-dot {
    0%,
    100% {
        opacity: 0.3;
        transform: scale(0.8);
    }

    50% {
        opacity: 1;
        transform: scale(1);
    }
}
</style>