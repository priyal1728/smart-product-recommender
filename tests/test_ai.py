from ai.query_parser import parse_user_query


def test_query_parser():

    query = """
    I need a smartphone under 30000 rupees.
    Camera is very important.
    I also want good battery life and strong gaming performance.
    """

    result = parse_user_query(query)

    assert result.category != ""
    assert result.budget > 0

    assert 0 <= result.camera_priority <= 1
    assert 0 <= result.battery_priority <= 1
    assert 0 <= result.performance_priority <= 1
    assert 0 <= result.display_priority <= 1