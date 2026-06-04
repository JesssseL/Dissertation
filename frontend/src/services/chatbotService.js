import { apiRequest } from './api/request'

export function getChatbotResponse(query, userMessage, conversationHistory) {
    return apiRequest('/api/chatbot', {
        method: 'POST',
        body: JSON.stringify({
            "query": query,
            "message": userMessage,
            "history": conversationHistory
        })
    })
}