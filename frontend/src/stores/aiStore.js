import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useAiStore = defineStore('ai', () => {
  const messages = ref([])
  const messageSending = ref(false)

  const hasMessages = computed(() => messages.value.length > 0)

  function sendStatusMessage(sender, text) { messages.value.push({ role: sender, content: text})}
  function sendUserMessage(text) { messages.value.push({role: 'user', content: text})}

  function addResults(results) {
    console.log('ai store addResults hit')
    messages.value = messages.value.filter(
      message => message.role !== 'system'
    )
    messages.value.push({
      role: 'system', 
      content: `Current product options: ${JSON.stringify(results)}`
    })
    messages.value.push({
      role: 'assistant', 
      content: `I've found ${results.length} options. Ask me about features, value, or differences between them.`
    })
  }

  async function sendAIMessage(text) {
    messages.value.push({role: 'assistant', content: ''})
    messageSending.value = true
    console.log('aiStore-test', text)
    const messageIndex = messages.value.length - 1
    for (let i = 0; i < text.length; i++) {
      const currentText = messages.value[messageIndex].content + text[i]
      messages.value.splice(messageIndex, 1, {
        role: 'assistant',
        content: currentText
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
    addResults,
    sendAIMessage,
    clearMessages
  }
})