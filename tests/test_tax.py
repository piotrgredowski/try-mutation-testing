import pytest

from src.tax import calculate_net_salary

@pytest.mark.parametrize("gross, expected_net", [(5000, 4062.0), (10000, 8124.0), (2000, 1624.8)])
def test_calculate_net_salary(gross, expected_net):
    assert calculate_net_salary(gross) == expected_net
