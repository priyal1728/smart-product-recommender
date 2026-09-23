from ai.explainer import explain_recommendations


def test_explainer():

    preferences = {
        "category": "smartphone",
        "budget": 30000,
        "camera_priority": 0.9,
        "battery_priority": 0.8,
        "performance_priority": 0.9,
        "display_priority": 0.5
    }

    products = [
        {
            "product_name": "OnePlus Nord 4",
            "price": 29999,
            "camera": 78,
            "battery": 90,
            "performance": 92,
            "display": 88,
            "score": 85.5
        }
    ]

    result = explain_recommendations(
        preferences,
        products
    )

    assert isinstance(result, str)
    assert len(result) > 0