"""Quantity API."""

from __future__ import annotations

from typing import Any, Protocol, runtime_checkable

import optype as op

type Unit = Any  # TODO: unit-api

__version__ = "0.0.1.dev0"
__all__ = ["Quantity"]

@runtime_checkable
class Quantity[V, U: Unit](Protocol):
    @property
    def value(self) -> V: ...
    @property
    def unit(self) -> U: ...

    ### Dunder Methods

    def __eq__[B: op.CanBool](
        self, other: Quantity[op.CanEq[V, B], U], /
    ) -> B: ...
