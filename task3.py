"""Создайте функцию генератор чисел Фибоначчи"""


def fib(n: int) -> list[int]:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


print(*fib(10))


# def fib1(limit: int):
#     fibo = [0, 1]
#     while limit > 0:
#         yield fibo[-1]
#         fibo.append(fibo[-1] + fibo[-2])
#         limit -= 1
#
#
# for number in fib1(10):
#     print(number)