export async function getRecommendationsMock(product, minPrice, maxPrice) {
    await new Promise(resolve => setTimeout(resolve, 3000))
    return [
            {
                "name": "AeroSound X1",
                "image": "https://picsum.photos/200/300?random=1",
                "features": ["Wireless", "Bluetooth 5.3", "Noise Cancelling"],
                "additionalFeatures": ["Deep Bass Mode", "Quick Charge", "Touch Controls"],
                "webUrl": "https://www.amazon.com/",
                "price": 129.99
            },
            {
                "name": "NovaBeat Pro",
                "image": "https://picsum.photos/200/300?random=2",
                "features": ["Wireless", "Bluetooth 5.3", "Noise Cancelling"],
                "additionalFeatures": ["Spatial Audio", "Voice Assistant Support", "Foldable Design"],
                "webUrl": "https://www.amazon.com/",
                "price": 179.99
            },
            {
                "name": "EchoWave Lite",
                "image": "https://picsum.photos/200/300?random=3",
                "features": ["Wireless", "Bluetooth 5.3", "Noise Cancelling"],
                "additionalFeatures": ["Lightweight Build", "30h Battery", "Sweat Resistant"],
                "webUrl": "https://www.amazon.com/",
                "price": 99.99
            }
        ]
}