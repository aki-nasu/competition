import math
def get_prime_list(n):
    prime = []
    limit = math.sqrt(n)
    data = [i for i in range(2, int(math.sqrt(n))+1)]
    print(data)
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]

print(get_prime_list(100))