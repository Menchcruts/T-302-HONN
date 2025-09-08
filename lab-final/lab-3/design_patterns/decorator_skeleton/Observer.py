from __future__ import annotations

from abc import ABC, abstractmethod

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Observable import Observable


class Observer(ABC):
    @abstractmethod
    def update(self, observable: Observable) -> None:
        pass
