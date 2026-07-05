def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    d = 3
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 2
    if n > 1:
        factors.append(n)
    return factors
n=56
print(prime_factors(n))
'''
По памяти занимает: O(log n)
По времени занимает: O(n**0.5) в наихудшем случае
Ограничения:
нет защиты от отрицательных и рациональных чисел
Достоинства:
наиболее быстрый способ решения задачи
'''