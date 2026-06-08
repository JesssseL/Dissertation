import { apiRequest } from './api/request'

export function addOrGetAccount(email, password) {
    return apiRequest('/api/account', {
        method: 'POST',
        body: JSON.stringify({
            "email": email,
            "password": password
        })
    })
}

export function addProduct(email, password, product){
    return apiRequest('/api/account/save-product', {
        method: 'POST',
        body: JSON.stringify({
            "email": email,
            "password": password,
            "product": product
        })
    })
} 

export function getProducts(email, password) {
    return apiRequest('/api/account/get-products', {
        method: 'POST',
        body: JSON.stringify({
            "email": email,
            "password": password
        })
    })
}