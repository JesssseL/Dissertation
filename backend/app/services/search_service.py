import random

def generate_budget_ranges(request):
    return [
        {
            "label": "Low",
            "min": 20,
            "max": 80
        },
        {
            "label": "Mid",
            "min": 80,
            "max": 200
        },
        {
            "label": "High",
            "min": 200,
            "max": 400
        }
    ]

def generate_recommendations(request):
    return [
        {
            "name": f"Everyday {request.query} XV",
            "image": "https://picsum.photos/200/300?random=1",
            "features": ["Eco-Friendly Packaging", "Portable", "Weather-Resistant"],
            "additionalFeatures": ["Extended Warranty", "Lifetime Support", "Free Shipping"],
            "webUrl": "https://www.amazon.com/",
            "price": round(random.uniform(request.minPrice, request.maxPrice), 2)
        },
        {
            "name": f"{request.query} Afterglow",
            "image": "https://picsum.photos/200/300?random=1",
            "features": ["Eco-Friendly Packaging", "Portable", "Weather-Resistant"],
            "additionalFeatures": ["Instant-Setup", "BPA-Free", "Scratch-Resistant"],
            "webUrl": "https://www.amazon.com/",
            "price": round(random.uniform(request.minPrice, request.maxPrice), 2)
        },
        {
            "name": f"Artisan's Choice {request.query}",
            "image": "https://picsum.photos/200/300?random=1",
            "features": ["Eco-Friendly Packaging", "Portable", "Weather-Resistant"],
            "additionalFeatures": ["Reinforced Stitching", "Fair-trade", "Hand-painted"],
            "webUrl": "https://www.amazon.com/",
            "price": round(random.uniform(request.minPrice, request.maxPrice), 2)
        },
    ]