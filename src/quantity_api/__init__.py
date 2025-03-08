"""Quantity API."""

from typing import Any, Final, Protocol, Self, runtime_checkable, Optional

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

    def __quantity_namespace__(
        self, /, *, api_version: Optional[str] = None
    ) -> Any:
        """
        Returns an object that has all the quantity API functions on it.

        Parameters
        ----------
        self: quantity
            quantity instance.
        api_version: Optional[str]
            string representing the version of the quantity API specification to be returned, in ``'YYYY.MM'`` form, for example, ``'2020.10'``. If it is ``None``, it should return the namespace corresponding to latest version of the quantity API specification.  If the given version is invalid or not implemented for the given module, an error should be raised. Default: ``None``.

        Returns
        -------
        out: Any
            an object representing the quantity API namespace. It should have every top-level function defined in the specification as an attribute. It may contain other public names as well, but it is recommended to only include those names that are part of the specification.
        """