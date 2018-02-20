from decimal import *

# This mode will return the total amount if it were to increase by a set amount.



def calculate_inc_mode(tuple_of_data,recent_coin_price):
    current_coin_price, current_user_percentage,command, command_number = tuple_of_data
    current_price = float(recent_coin_price)
    percentage_to_compare = float(current_user_percentage)
    Projected_increase = percentage_to_compare * current_price
    Add_To_Total = current_price + Projected_increase
    return Add_To_Total


def calculate_dec_mode(current_coin_price, percentage_increase):
    current_price = float(current_coin_price)
    percentage_to_compare = float(percentage_increase)
    Projected_decrease = percentage_to_compare * current_price
    Decrease_From_Total = current_price - Projected_decrease
    return Decrease_From_Total
