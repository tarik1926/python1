def get_total_ways(coins: list, amount: int) -> int:
    """Calculates how many different combinations of coins sum up to the amount."""
    dp = [0] * (amount + 1)
    
    dp[0] = 1
    
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = dp[i] + dp[i - coin]
            
    return dp[amount]


def get_minimum_coins(coins: list, amount: int) -> int:
    """Calculates the minimum number of coins needed to make the amount."""
    dp = [float('inf')] * (amount + 1)
    
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
                
    return dp[amount] if dp[amount] != float('inf') else -1

coins_list = [1, 2, 5, 10]
target_sum = 10

ways = get_total_ways(coins_list, target_sum)
min_coins = get_minimum_coins(coins_list, target_sum)

print(f"Target Sum: {target_sum}")
print(f"Available Coins: {coins_list}")
print("-" * 30)
print(f"Total different ways to make {target_sum}: {ways}")
print(f"Minimum coins needed to make {target_sum}: {min_coins}")