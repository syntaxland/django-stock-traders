import random

def generate_trader_data():
    traders = ['trader1', 'trader2', 'trader3', 'trader4', 'trader5',
               'trader6', 'trader7', 'trader8', 'trader9', 'trader10']
    trader_data = {}

    for trader in traders:
        data_points = []
        initial_amount = 100
        for _ in range(60):
            profit_loss = round(random.uniform(-10, 10), 2)
            data_points.append(profit_loss)
        trader_data[trader] = data_points

    return trader_data





trader_data = generate_trader_data()
print(trader_data)
