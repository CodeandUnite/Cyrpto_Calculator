import pytest
'''
We hope by using this test that we will make sure the math functionality
is correct for the program
'''


from decimal import *






def calculate_inc_mode(price, percentage_increase):

    cyrpto_price = float(price)
    # Change to percentage_to_increase
    percentage_to_increase = float(percentage_increase)
    projectedIncrease = cyrpto_price * percentage_to_increase
    AddToTotal = cyrpto_price + projectedIncrease
    return AddToTotal

def test_calulate_inc_mode():
    assert calculate_inc_mode(10000,0.10) == 11000
    assert calculate_inc_mode(10000,0.20) == 12000
    assert calculate_inc_mode(10000,0.30) == 13000
    assert calculate_inc_mode(10000,0.40) == 14000
    assert calculate_inc_mode(10000,0.50) == 15000
    assert calculate_inc_mode(10000,0.60) == 16000
    assert calculate_inc_mode(10000,0.70) == 17000
    assert calculate_inc_mode(10000,0.80) == 18000
    assert calculate_inc_mode(10000,0.90) == 19000
    assert calculate_inc_mode(10000,0.77) == 17700

def calculate_dec_mode(price, percentage_decrease):
    cyrpto_price = float(price)
    percentage_to_decrease = float(percentage_decrease)
    Projected_decrease = cyrpto_price * percentage_to_decrease
    Decrease_From_Total = cyrpto_price - Projected_decrease
    return Decrease_From_Total

def test_calulate_dec_mode():
    assert calculate_dec_mode(10000, 0.10) == 9000
    assert calculate_dec_mode(10000, 0.20) == 8000
    assert calculate_dec_mode(10000, 0.30) == 7000
    assert calculate_dec_mode(10000, 0.40) == 6000
    assert calculate_dec_mode(10000, 0.50) == 5000
    assert calculate_dec_mode(10000, 0.60) == 4000
    assert calculate_dec_mode(10000, 0.70) == 3000
    assert calculate_dec_mode(10000, 0.80) == 2000
    assert calculate_dec_mode(10000, 0.90) == 1000
    assert calculate_dec_mode(800000000, 0.33) == 536000000
