import pytest
'''
We hope by using this test that we will make sure the math functionality
is correct for the program
'''


from decimal import *


cyrpto = "btc"
fiat = "usd"
percentage = "10"
price = "10000"

dataTuple = (cyrpto, fiat, percentage, price)

def calculate_inc_mode(dataTuple):
    from model import bitcoin
    cyrpto, fiat, percentage_increase, price = dataTuple
    cyrpto_price = float(price)
    # Change to percentage_to_increase
    current_price = float(percentage_increase)
    projectedIncrease = cyrpto_price * current_price
    AddToTotal = current_price + projectedIncrease
    return AddToTotal

def test_calulate_inc_mode():

    price_one = 10000
    price_two = 30000
    price_two = 60000

    ten_percentage = 0.10
    twenty_percentage = 0.20
    thirty_percentage = 0.30
    fourty_percentage = 0.40
    fifty_percentage = 0.50
    sixty_percentage = 0.60
    seventy_percentage = 0.70
    eighty_percentage = 0.80
    nienty_percentage = 0.90
    hundred_percentage = 0.100


    cyrpto_price_test1 = float(price_one)

    percentage_to_increase1 = float(ten_percentage)
    percentage_to_increase2 = float(twenty_percentage)
    percentage_to_increase3 = float(thirty_percentage)
    percentage_to_increase4 = float(fourty_percentage)
    percentage_to_increase5 = float(fifty_percentage)
    percentage_to_increase6 = float(sixty_percentage)
    percentage_to_increase7 = float(seventy_percentage)
    percentage_to_increase8 = float(eighty_percentage)
    percentage_to_increase9 = float(nienty_percentage)
    percentage_to_increase10 = float(hundred_percentage)
    Calculated_projected_increase1 = cyrpto_price_test1 * percentage_to_increase1
    Calculated_projected_increase2 = cyrpto_price_test1 * percentage_to_increase2
    Calculated_projected_increase3 = cyrpto_price_test1 * percentage_to_increase3
    Calculated_projected_increase4 = cyrpto_price_test1 * percentage_to_increase4
    Calculated_projected_increase5 = cyrpto_price_test1 * percentage_to_increase5
    Calculated_projected_increase6 = cyrpto_price_test1 * percentage_to_increase6
    Calculated_projected_increase7 = cyrpto_price_test1 * percentage_to_increase7
    Calculated_projected_increase8 = cyrpto_price_test1 * percentage_to_increase8
    Calculated_projected_increase9 = cyrpto_price_test1 * percentage_to_increase9
    Calculated_projected_increase10 = cyrpto_price_test1 * percentage_to_increase10

    AddToTotal1 = cyrpto_price_test1 + Calculated_projected_increase1
    AddToTotal2 = cyrpto_price_test1 + Calculated_projected_increase2
    AddToTotal3 = cyrpto_price_test1 + Calculated_projected_increase3
    AddToTotal4 = cyrpto_price_test1 + Calculated_projected_increase4
    AddToTotal5 = cyrpto_price_test1 + Calculated_projected_increase5
    AddToTotal6 = cyrpto_price_test1 + Calculated_projected_increase6
    AddToTotal7 = cyrpto_price_test1 + Calculated_projected_increase7
    AddToTotal8 = cyrpto_price_test1 + Calculated_projected_increase8
    AddToTotal9 = cyrpto_price_test1 + Calculated_projected_increase9
    AddToTotal10 = cyrpto_price_test1 + Calculated_projected_increase10


    assert AddToTotal1 == 11000
    assert AddToTotal2 == 12000
    assert AddToTotal3 == 13000
    assert AddToTotal4 == 14000
    assert AddToTotal5 == 15000
    assert AddToTotal6 == 16000
    assert AddToTotal7 == 17000
    assert AddToTotal8 == 18000
    assert AddToTotal9 == 19000


def calculate_dec_mode(dataTuple):
    from model import bitcoin
    cyrpto, fiat, percentage_increase, price = dataTuple
    cyrpto_price = float(price)
    current_price = float(percentage_increase)

    Projected_decrease = cyrpto_price * current_price
    Decrease_From_Total = current_price - Projected_decrease
    return Decrease_From_Total
