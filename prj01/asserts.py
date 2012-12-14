def assert_approx(expected, actual, tolerance=1e-6):
    assert abs(expected - actual) <= tolerance

def assert_str(expected, obj):
    assert expected == str(obj)