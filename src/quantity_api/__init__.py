"""Quantity API."""

from __future__ import annotations

from typing import Any, Protocol, TypeAlias, runtime_checkable

type Unit = Any  # TODO: unit-api

__version__ = "0.0.1.dev0"
__all__ = ["Quantity"]

@runtime_checkable
class Quantity[V, U: Unit](Protocol):
    @property
    def value(self) -> V: ...
    @property
    def unit(self) -> U: ...

    def __init__(self, value: V, unit: U, **kw: Any) -> Quantity[V, U]: ...

    def to_unit(self, unit: U, /, **kw: Any) -> Quantity[V, U]: ...

    ### Dunder Methods

    def __eq__(self, other: Quantity[V, U]): ...
