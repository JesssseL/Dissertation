import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useAiStore = defineStore('ai', () => {
  const messages = ref([])
  const messageSending = ref(false)

  const hasMessages = computed(() => messages.value.length > 0)

  function sendStatusMessage(sender, text) { messages.value.push({sender, text})}
  function sendUserMessage(text) { messages.value.push({sender: 'user', text})}

  async function sendAIMessage(text) {
    messages.value.push({sender: 'ai', text: ''})
    messageSending.value = true

    const messageIndex = messages.value.length - 1
    for (let i = 0; i < text.length; i++) {
      const currentText = messages.value[messageIndex].text + text[i]
      messages.value.splice(messageIndex, 1, {
        sender: 'ai',
        text: currentText
      })
      await new Promise(resolve => setTimeout(resolve, 25))
    }
    messageSending.value = false
  }

  function clearMessages() {
    messages.value = []
  }

  return {
    messages,
    messageSending,
    hasMessages,
    sendStatusMessage,
    sendUserMessage,
    sendAIMessage,
    clearMessages
  }
})