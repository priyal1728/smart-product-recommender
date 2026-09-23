from fuzzy.fuzzy_engine import calculate_fuzzy_score


def test_fuzzy_score():
    score = calculate_fuzzy_score(
        camera=90,
        battery=90,
        performance=90,
        price=90
    )

    assert 0 <= score <= 100