import pandas as pd

from fuzzy.fuzzy_engine import calculate_fuzzy_score


def calculate_price_score(product_price, budget):
    """
    Convert product price into a 0-100 suitability score.
    """

    if product_price <= budget:
        difference = budget - product_price

        if budget == 0:
            return 0

        score = 100 - (difference / budget) * 30
        return max(70, score)

    difference = product_price - budget
    penalty = (difference / budget) * 100

    return max(0, 70 - penalty)


def recommend_products(preferences, csv_path="data/products.csv"):
    """
    Generate product recommendations using fuzzy logic.
    """

    products = pd.read_csv(csv_path)

    recommendations = []

    for _, product in products.iterrows():

        price_score = calculate_price_score(
            product["price"],
            preferences.budget
        )

        fuzzy_score = calculate_fuzzy_score(
            camera=product["camera"],
            battery=product["battery"],
            performance=product["performance"],
            price=price_score
        )

        final_score = (
            fuzzy_score
            * (
                preferences.camera_priority
                + preferences.battery_priority
                + preferences.performance_priority
                + preferences.display_priority
            )
            / 4
        )

        recommendations.append({
            "product_id": product["product_id"],
            "product_name": product["product_name"],
            "price": product["price"],
            "camera": product["camera"],
            "battery": product["battery"],
            "performance": product["performance"],
            "display": product["display"],
            "score": round(final_score, 2)
        })

    recommendations.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return recommendations