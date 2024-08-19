"""
Exercise 3 - A Greedy Algorithm
"""


def findGreatestProfit(stockArray):    
    buy_price = stockArray[0]
    greatest_profit = 0
    
    for price in stockArray:
        potential_profit = price - buy_price
        
        if price < buy_price:
            buy_price = price
        elif potential_profit > greatest_profit:
            greatest_profit = potential_profit
            
    return greatest_profit
            
                

if __name__ == '__main__':
    stocks = [10, 7, 5, 8, 11, 2, 6]
    
    print(findGreatestProfit(stocks))
        