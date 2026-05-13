import { apiRequest } from './api/request'
import { getProductFeaturesMock } from './mocks/productMock'
import { getBudgetRangesMock } from './mocks/productMock'

export function getProductFeatures(query) {
    return getProductFeaturesMock(query)
    //return apiRequest('product/features', query)
}

export function getBudgetRanges(query) {
    return getBudgetRangesMock(query)
    //return apiRequest('product/budget-ranges', query)
}