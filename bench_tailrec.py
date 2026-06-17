import sys
from typing import Callable
from tailrec import Recurrent, Thunkable, Generatable, trampoline, trampoline_generator
import timeit


@Recurrent
def fact_cps_tailrec[T](n: int, k: Recurrent[[int], T]) -> T:
    if n == 0:
        return k(1)
    else:

        @Recurrent
        def go(value: int) -> T:
            k.recur(n * value)

        fact_cps_tailrec.recur(n - 1, go)


def fact_cps_thunked[T](n: int, k: Callable[[int], Thunkable[T]]) -> Thunkable[T]:
    if n == 0:
        return k(1)
    else:
        return lambda: fact_cps_thunked(n - 1, lambda value: lambda: k(n * value))


def fact_cps_gen[T](n: int, k: Callable[[int], Generatable[T]]) -> Generatable[T]:
    if n == 0:
        yield k(1)
    else:

        def go(value: int) -> Generatable[T]:
            yield k(n * value)

        yield fact_cps_gen(n - 1, go)


@Recurrent
def tailrec_test() -> int:
    return fact_cps_tailrec.recur(
        sys.getrecursionlimit() * 2, Recurrent(lambda value: value)
    )


def trampoline_thunked_test() -> int:
    def k(value: int) -> int:
        return value

    return trampoline(fact_cps_thunked, sys.getrecursionlimit() * 2, k)


def trampoline_generator_test() -> int:
    def k(value: int) -> Generatable[int]:
        yield value

    return trampoline_generator(fact_cps_gen, sys.getrecursionlimit() * 2, k)


result = timeit.timeit(tailrec_test, number=300)
average_result = result / 300
print(f"Average result for tailrec: {average_result:.3f} seconds")
result = timeit.timeit(trampoline_thunked_test, number=300)
average_result = result / 300
print(f"Average result for trampoline thunked: {average_result:.3f} seconds")
result = timeit.timeit(trampoline_generator_test, number=300)
average_result = result / 300
print(f"Average result for trampoline generator: {average_result:.3f} seconds")


def sum_gen(acc: int, n: int) -> Generatable[int]:
    if n == 0:
        yield acc
    else:
        yield sum_gen(n + acc, n - 1)


def sum_thunked(acc: int, n: int) -> Thunkable[int]:
    if n == 0:
        return acc
    return lambda: sum_thunked(n + acc, n - 1)


def sum_normal(n: int) -> int:
    summed = 0
    for i in range(0, n + 1):
        summed += i
    return summed


def test_gen() -> int:
    return trampoline_generator(sum_gen, 0, 50000)


def test_thunked() -> int:
    return trampoline(sum_thunked, 0, 50000)


def test_normal() -> int:
    return sum_normal(50000)


result = timeit.timeit(test_normal, number=1000)
average_result = result / 1000
print(f"Average result for normal: {average_result:.3f} seconds")
result = timeit.timeit(test_thunked, number=1000)
average_result = result / 1000
print(f"Average result for thunked: {average_result:.3f} seconds")
result = timeit.timeit(test_gen, number=1000)
average_result = result / 1000
print(f"Average result for generator: {average_result:.3f} seconds")
