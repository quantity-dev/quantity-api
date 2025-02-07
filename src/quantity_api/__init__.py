"""Quantity API."""

from typing import Any, Final, Protocol, Self, runtime_checkable

import optype as op

type Unit = Any  # TODO: unit-api

__version__: Final = "0.0.1.dev0"
__all__ = ["__version__", "Quantity"]

@runtime_checkable
class Quantity[V, U: Unit](Protocol):
    @property
    def value(self) -> V: ...
    @property
    def unit(self) -> U: ...

    ### Dunder Methods

    def __eq__[B](self, other: Self[op.CanEq[V, B], U], /) -> B: ...
