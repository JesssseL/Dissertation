import { apiRequest } from './api/request'

export function getProductFeatures(query) {
    return apiRequest('/api/features', {
        method: 'POST',
        body: JSON.stringify({
            "query": query
        })
    })
}

export function getProductPhotos(query){
    return apiRequest('/api/photos', {
        method: 'POST',
        body: JSON.stringify({
            "query": query
        })
    })
} 

export function getProductQuestions(query) {
    return apiRequest('/api/questions', {
        method: 'POST',
        body: JSON.stringify({
            "query": query
        })
    })
}

export function getBudgetRanges(query) {
    return apiRequest('/api/budget-ranges', {
        method: 'POST',
        body: JSON.stringify({
            "query": query
        })
    })
}