import sys
from typing import Callable
from tailrec import Recurrent, Thunkable, trampoline


@Recurrent
def fact_cps_tailrec[T](n: int, k: Recurrent[[int], T]) -> T:
    if n == 0:
        return k(1)
    else:

        @Recurrent
        def go(value: int) -> T:
            k.recur(n * value)

        fact_cps_tailrec.recur(n - 1, go)


import timeit


def fact_cps_thunked[T](n: int, k: Callable[[int], Thunkable[int]]) -> Thunkable[int]:
    if n == 0:
        return k(1)
    else:
        return lambda: fact_cps_thunked(n - 1, lambda value: lambda: k(n * value))


@Recurrent
def tailrec_test() -> int:
    return fact_cps_tailrec.recur(
        sys.getrecursionlimit() * 2, Recurrent(lambda value: value)
    )


def trampoline_test() -> int:
    def k(value: int) -> int:
        return value

    return trampoline(fact_cps_thunked, sys.getrecursionlimit() * 2, k)


result = timeit.timeit(tailrec_test, number=100)
average_result = result / 100
print(f"Average result for tailrec: {average_result:.3f} seconds")
result = timeit.timeit(trampoline_test, number=100)
average_result = result / 100
print(f"Average result for trampoline: {average_result:.3f} seconds")


def sum_thunked(acc: int, n: int) -> Thunkable[int]:
    if n == 0:
        return acc
    return lambda: sum_thunked(n + acc, n - 1)


def sum_normal(n: int) -> int:
    summed = 0
    for i in range(0, n + 1):
        summed += i
    return summed


def test_thunked() -> int:
    return trampoline(sum_thunked, 0, 50000)


def test_normal() -> int:
    return sum_normal(50000)


result = timeit.timeit(test_thunked, number=1000)
average_result = result / 1000
print(f"Average result for thunked: {average_result:.3f} seconds")
result = timeit.timeit(test_normal, number=1000)
average_result = result / 1000
print(f"Average result for normal: {average_result:.3f} seconds")
