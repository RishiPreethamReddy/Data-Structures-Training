def possible(coins,t):
    dp=[False]*(t+1)
    dp[0]=True
    for i in coins:
        for j in range(i,t+1):
            if dp[j-i]:
                dp[j]=True
    return dp[t]

coins=[2,3,5,6]
t=7
print(possible(coins,t)) 
