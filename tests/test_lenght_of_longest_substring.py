from algorithm_practice.arrays_algorithms import lenght_of_longest_substring

def test_lenght_of_longest_substring_abcabcbb_returns_3():
    s = "abcabcbb" 

    result =lenght_of_longest_substring(s)

    assert result == 3

def test_lenght_of_longest_substring_bbbbb_returns_1():
    s = "bbbbb" 

    result =lenght_of_longest_substring(s)

    assert result == 1

def test_lenght_of_longest_substring_pwwkew_returns_3():
    s = "pwwkew" 

    result =lenght_of_longest_substring(s)

    assert result == 3

def test_lenght_of_longest_substring_blank_space_returns_1():
    s = " " 

    result =lenght_of_longest_substring(s)

    assert result == 1

def test_lenght_of_longest_substring_dvdf_returns_3():
    s = "dvdf" 

    result =lenght_of_longest_substring(s)

    assert result == 3