abc = [int(input()) for _ in range(3)]
ranking = [2,2,2]
ranking[abc.index(max(abc))] = 1
ranking[abc.index(min(abc))] = 3
for i in range(3): print(ranking[i])