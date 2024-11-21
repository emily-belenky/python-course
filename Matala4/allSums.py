def allSumsDP(arr):
    length = len(arr)
    dp = []
    for num in range(length + 1):
        dp.append(set())
    dp[0].add(0)
    for i in range(1, length+1):
        for j in dp[i-1]:
            dp[i].add(j)
            dp[i].add(j+arr[i-1])
    return dp[length]