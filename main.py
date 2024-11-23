def test_should_return_area():
    assert rectangle_area(5, 10) == 50
    assert rectangle_area(0, 10) == 0
    try:
        rectangle_area(-5, 10)
    except ValueError as e:
        assert str(e) == "Length and width must be non-negative."
