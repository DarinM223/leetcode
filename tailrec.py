# type: ignore
from typing import Callable, ParamSpec, TypeVar, Generic, NoReturn

P = ParamSpec("P")
T = TypeVar("T")


class Recur(BaseException, Generic[P, T]):
    f: Callable[P, T]

    def __init__(self, f: Callable[P, T], args: P.args, kwargs: P.kwargs):
        super().__init__()
        self.f = f.f if isinstance(f, Recurrent) else f
        self.args = args
        self.kwargs = kwargs

    def __call__(self) -> T:
        return self.f(*self.args, **self.kwargs)

    def __repr__(self) -> str:
        if self.kwargs:
            return f"<Recur {self.f.__name__}(*{self.args}, **{self.kwargs})>"
        return f"<Recur {self.f.__name__}{self.args})>"

    __str__ = __repr__


class Recurrent(Generic[P, T]):
    f: Callable[P, T]

    def __init__(self, f: Callable[P, T]) -> None:
        self.f = f

    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> T:
        r = Recur(self.f, args, kwargs)
        while True:
            try:
                return r()
            except Recur as exc:
                r = exc

    def recur(self, *args: P.args, **kwargs: P.kwargs) -> NoReturn:
        raise Recur(self.f, args, kwargs)

    def __repr__(self) -> str:
        return f"<Recurrent {self.f.__name__}>"


type Thunkable[T] = T | Callable[[], Thunkable[T]]


def trampoline[**P, T](
    f: Callable[P, Thunkable[T]], *args: P.args, **kwargs: P.kwargs
) -> T:
    v = f(*args, **kwargs)
    while callable(v):
        v = v()
    return v  # type: ignore
