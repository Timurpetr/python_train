SashaCoins = set(map(int, input().split()))
GalyaCoins = list(map(int, input().split()))

print(*sorted(filter(lambda x: x in GalyaCoins and x % 2 == 0,SashaCoins)))