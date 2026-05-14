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