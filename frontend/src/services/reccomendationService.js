import { apiRequest } from './api/request'

export function getRecommendations(query, minPrice, maxPrice) {
    return apiRequest('/api/recommendations', {
        method: 'POST',
        body: JSON.stringify({
            "query": query,
            "minPrice": minPrice,
            "maxPrice": maxPrice
        })
    })
}