"""
Recognizing Patterns - Optimized The Coin Game - by Generating Examples

Algorithm: Page 409

Time complexity: O(1)
"""


def game_winner(number_of_coins):
    if (number_of_coins  - 1) % 3 == 0:
        return 'them'
    else:
        return 'you'
    

if __name__ == '__main__':
    coins = 4
    
    print(game_winner(coins))
    