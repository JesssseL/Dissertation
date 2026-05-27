import { apiRequest } from './api/request'

export function getRecommendations(query, minPrice, maxPrice, features) {
    console.log('api reccomendations', query, minPrice, maxPrice, features)
    return apiRequest('/api/recommendations', {
        method: 'POST',
        body: JSON.stringify({
            "query": query,
            "minPrice": minPrice,
            "maxPrice": maxPrice,
            "features": features
        })
    })
}

export function getNewQueryFromQuestionAnswers(query, questionsAndAnswers) {
    console.log('api answers', query, questionsAndAnswers)
    return apiRequest('/api/answers', {
        method: 'POST',
        body: JSON.stringify({
            "query": query,
            "questionsAndAnswers": questionsAndAnswers,
        })
    })
}

export function getNewQueryFromPhotosSelected(query, photos) {
    console.log('api photos', query, photos)
    return apiRequest('/api/photo-features', {
        method: 'POST',
        body: JSON.stringify({
            "query": query,
            "products": photos,
        })
    })
}