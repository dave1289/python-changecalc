def get_change():
	total_cost = int(input('Enter total cost:  '))
	increments = [100, 25, 10, 5, 1]
	change_totals = {}
	for change in increments:
		if total_cost >= 100:
			num_dollars = total_cost // change
			total_cost -= num_dollars * change
			change_totals['dollars'] = num_dollars
		if total_cost >= 25:
			num_quarters = total_cost // change
			total_cost -= num_quarters * change
			change_totals['quarters'] = num_quarters
		if total_cost >= 10:
			num_dimes = total_cost // change
			total_cost -= num_dimes * change
			change_totals['dimes'] = num_dimes
		if total_cost >= 5:
			num_nickels = total_cost // change
			total_cost -= num_nickels * change
			change_totals['nickels'] = num_nickels
		else:
			num_pennies = total_cost // change
			change_totals['pennies'] = num_pennies
	change_totals = {x: y for x, y in change_totals.items() if y != 0}

	return change_totals


def present_change(change_dict):
	for k, v in change_dict.items():
		if v == 1:
			if k == 'pennies':
				k = 'pennys'
			# 	enjoy the pennys
			k = k[:-1:]
		print(f'You have {v} {k}.')


present_change(get_change())

