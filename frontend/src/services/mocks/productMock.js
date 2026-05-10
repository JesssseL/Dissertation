export async function getProductFeaturesMock(query) {
    await new Promise(resolve => setTimeout(resolve, 3000))
    return [
            'Battery life',
            'Noise cancellation',
            'Comfort',
            'Brand reputation',
            'Portability'
        ]
}

export async function getBudgetRangesMock(query) {
    await new Promise(resolve => setTimeout(resolve, 3000))
    return [
            { label: 'Low', min: 20, max: 80 },
            { label: 'Mid', min: 80, max: 200 },
            { label: 'High', min: 200, max: 400 }
        ]
}