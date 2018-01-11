
# This mode will return the total amount if it were to increase by a set amount.
def calculate_v_mode(current_coin_price, user_amount_var):
	current_price = float(current_coin_price)
	current_amount = float(user_amount_var)
	v_amount =  current_price * current_amount
	return v_amount

def calculate_inc_mode(current_coin_price, percentage_increase):
	current_price = float(current_coin_price)
	percentage_increase = Decimal(percentage_increase)
	print current_price * percentage_increase

