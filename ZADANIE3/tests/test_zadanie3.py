import pytest
import sys
import os

from ZADANIE3.zadanie3 import find_crossovers, calculate_total_btc_traded

def test_find_crossovers():
    """Test that find_crossovers returns the correct list of crossover dates."""
    expected_dates = ['2024-08-10', '2024-10-28', '2025-04-07', '2025-05-22', '2025-11-16']
    result = find_crossovers()
    assert result == expected_dates, f"Expected {expected_dates}, but got {result}"


def test_calculate_total_btc_traded():
    """Test that calculate_total_btc_traded returns the correct maximum volume."""
    expected_volume = 2018672
    result = calculate_total_btc_traded()
    assert result == expected_volume, f"Expected {expected_volume}, but got {result}"

