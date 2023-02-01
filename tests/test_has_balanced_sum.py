from algorithm_practice.arrays_algorithms import has_balanced_sum, get_balanced_sum_index
def test_has_balanced_sum_balanced_arrays_inputs():
   array1 = [ 2, 4, 1, 7 ]
   array2 = [ 5, 3, 1, 7 ]

   assert has_balanced_sum(array1)
   assert has_balanced_sum(array2)

def test_has_balanced_sum_unbalanced_array_input():
    array = [ 2, 4, 1, 3, 8 ]

    assert not has_balanced_sum(array)

def test_get_balanced_sum_index_balanced_input():
    array = [ 2, 4, 1, 5, 7 ]

    result = get_balanced_sum_index(array)

    assert result== 3

def test_get_balanced_sum_index_unbalanced_input():
    array = [ 5, 3, 1, 7 ]

    result = get_balanced_sum_index(array)

    assert result is None

def test_get_balanced_sum_index_simetrical_input_return_none():
    array = [ 10,10]

    result = get_balanced_sum_index(array)

    assert result is None


