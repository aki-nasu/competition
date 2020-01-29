n,d,a = map(int,input().split())
monsters = [tuple(map(int,input().split())) for _ in range(n)]
monsters.sort()

# 各モンスターを倒すためにおこなった攻撃回数を記録する
# atk_count[1]が2の場合、x2番目のモンスターに対して2回攻撃をおこなったことを意味する
atk_count = [0]*n
atk_count_sum = 0
l = 0 # 左端
for i in range(n):
    x = monsters[i][0]
    h = monsters[i][1]
    # 尺取り法
    while monsters[l][0] + 2*d < x:
        atk_count_sum -= atk_count[l]
        l += 1
    # 既に受けているダメージ
    al = atk_count_sum * a
    h = h - al
    if h > 0:
        atk_count[i] = -(-h//a)
    atk_count_sum += atk_count[i]
print(sum(atk_count))