from decimal import *

# This mode will return the total amount if it were to increase by a set amount.


def calculate_v_mode(current_coin_price, user_amount_var):
    current_price = float(current_coin_price)
    current_amount = float(user_amount_var)
    v_amount = current_price * current_amount
    return v_amount


def calculate_inc_mode(current_coin_price, percentage_increase):
    current_price = float(current_coin_price)
    percentage_to_compare = float(percentage_increase)
    Projected_increase = percentage_to_compare * current_price
    Add_To_Total = current_price + Projected_increase
    return Add_To_Total


def calculate_dec_mode(current_coin_price, percentage_increase):
    current_price = float(current_coin_price)
    percentage_to_compare = float(percentage_increase)
    Projected_decrease = percentage_to_compare * current_price
    Decrease_From_Total = current_price - Projected_decrease
    return Decrease_From_Total
