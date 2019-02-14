

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
                         'hypothyroidism')
                         ])
def test_TSH_diagnosis(a, expected):
    from TSH_data_conv import TSH_diagnosis
    answer = TSH_diagnosis(a)
    assert answer == expected
