from algorithm_practice.string_algorithms import camelcase

def test_camelcase_camelcase_string():
    s = "camelCaseString"

    result = camelcase(s)

    assert result == 3