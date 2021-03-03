#! /usr/bin/env python

"""
This program generates a dictionary 'profit' containing the cost price per unit,
sell price per unit, and the starting inventory. Assuming all inventory has been
sold, this program will return the profit rounded to the nearest dollar.
User should input the inventory (integers only), cost and sell price can be integers
or float.
"""

def get_inventory():
    try:
        inventory = input("Please enter the starting inventory: ")
        return int(inventory)
    except ValueError:
        print("Only integer numbers are accepted")
        return get_inventory()

def get_prices():
    try:
        cost_price = input("Please enter the cost price per unit (USD): ")
        sell_price = input("Please enter the sell price per unit (USD): ")
        return float(cost_price), float(sell_price)
    except ValueError:
        print("Only numbers are accepted")
        return get_prices()

def calc_profit(profit):
    calc_cost = profit['Inventory']*profit['Cost price']
    calc_sell = profit['Inventory']*profit['Sell price']
    return int(calc_sell-calc_cost)

if __name__ == '__main__':
    inventory = get_inventory()
    cost_price, sell_price = get_prices()
    profit = {'Inventory': inventory, 'Cost price': cost_price, 'Sell price': sell_price}
    print("Profit: ", calc_profit(profit))
