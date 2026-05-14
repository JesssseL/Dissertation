import { apiRequest } from './api/request'
import { getProductFeaturesMock } from './mocks/productMock'

export function getProductFeatures(query) {
    return getProductFeaturesMock(query)
    //return apiRequest('product/features', query)
}

export function getBudgetRanges(query) {
    console.log('query', query)
    return apiRequest('/api/budget-ranges', {
        method: 'POST',
        body: JSON.stringify({
            "query": query
        })
    })
}