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
            { label: 'Budget', min: 20, max: 80 },
            { label: 'Mid-range', min: 80, max: 200 },
            { label: 'Premium', min: 200, max: 400 }
        ]
}