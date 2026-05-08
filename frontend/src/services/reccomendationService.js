import { apiRequest } from './api/request'
import { getReccomendationsMock } from './mocks/reccomendationMock'

export function getReccomendations(query) {
    return getReccomendationsMock(query)
    //return apiRequest('reccomendation/results', query)
}