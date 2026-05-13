import { apiRequest } from './api/request'
import { getRecommendationsMock } from './mocks/reccomendationMock'

export function getRecommendations(query, minPrice, maxPrice) {
    return getRecommendationsMock(query, minPrice, maxPrice)
    //return apiRequest('reccomendation/results', query)
}