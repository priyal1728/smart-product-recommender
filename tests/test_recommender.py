from ai.query_parser import UserPreferences
from recommendation.recommender import recommend_products


def test_recommend_products():

    preferences = UserPreferences(
        category="smartphone",
        budget=30000,
        camera_priority=0.9,
        battery_priority=0.8,
        performance_priority=0.9,
        display_priority=0.5
    )

    results = recommend_products(preferences)

    assert len(results) > 0
    assert "product_name" in results[0]
    assert "score" in results[0]
    assert 0 <= results[0]["score"] <= 100