import { apiRequest } from './api/request'
import { getRecommendationsMock } from './mocks/reccomendationMock'

export function getRecommendations(product, minPrice, maxPrice) {
    return getRecommendationsMock(product, minPrice, maxPrice)
    //return apiRequest('reccomendation/results', query)
}