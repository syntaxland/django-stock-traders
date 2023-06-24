import random
from decimal import Decimal

def generate_trader_data():
    traders = ['Trader 1', 'Trader 2', 'Trader 3', 'Trader 4', 'Trader 5', 'Trader 6', 'Trader 7', 'Trader 8', 'Trader 9', 'Trader 10']
    trader_data = []

    for trader in traders:
        profit_loss = Decimal(random.uniform(-10, 10)).quantize(Decimal('0.00'))
        trader_data.append({
            'trader': trader,
            'profit_loss': profit_loss,
        })

    return trader_data
