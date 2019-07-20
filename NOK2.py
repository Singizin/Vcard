def nok(a, b):
    n = min(a, b)
    while True:
        if n % a == 0 and n % b == 0:
            break
        n = n + 1
    return n

print(nok(6,8))