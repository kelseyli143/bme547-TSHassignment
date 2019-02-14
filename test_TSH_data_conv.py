

import pytest


@pytest.mark.parametrize("a, expected", [
                         ([3.5, 3.6, 1.8, 2.8, 1.9, 3.4, 3, 3.6, 3, 4],
                          'normal thyroid function'),
                         ([2.7, 1.4, 3.1, 0.4, 1.8, 3.1, 3, 3.8, 0.9, 2.3],
                          'hyperthyroidism'),
                         ([2.5, 1.1, 1.3, 2.7, 1.9, 2.6, 3.5, 1, 1.4],
                          'normal thyroid function'),
                         ([6.3, 6.7, 6.3, 7.6, 2.1, 6.9, 4.1, 7.2, 3.5, 2.9],
                          'hypothyroidism'),
                         ([7, 4.6, 5.2, 2.3, 6.1, 4.4],
                          'hypothyroidism'),
                         ([0.2, 0.4, 0.5, 0.7, 0.8, 1.5, 1.8, 2.0, 2.2, 2.4,
                           2.5, 2.7, 2.8, 2.9, 3.8],
                          'hyperthyroidism'),
                         ([1.1, 2.0, 2.1, 2.4, 2.4, 3.0, 3.5, 3.7, 3.9],
                          'normal thyroid function'),
                         ([2.4, 2.5, 2.7, 3.3, 4.5, 5.2, 5.2, 5.3, 5.8],
                          'hypothyroidism'),
                         ([0.2, 0.2, 0.2, 0.5, 0.6, 0.6, 1.0, 1.1, 1.5, 2.2,
                           3.5, 3.5, 3.5, 3.5, 3.7],
                          'hyperthyroidism'),
                         ([0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2],
                          'hyperthyroidism'),
                         ([3.2], 'normal thyroid function'),
                         ([0.1, 0.7, 1.3, 1.7, 3.2, 3.2],
                          'hyperthyroidism')
                         ])
def test_TSH_diagnosis(a, expected):
    """Tests the TSH_diagnosis function

    Args:
        a (list): the patient's TSH values, is a list of floats
        expected (string): the expected diagnosis based on TSH values
    """
    from TSH_data_conv import TSH_diagnosis
    answer = TSH_diagnosis(a)
    assert answer == expected
