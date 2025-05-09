from abc import ABC, abstractmethod
from typing import Self


class CommandSource(ABC):
    def __aiter__(self) -> Self:
        return self

    @abstractmethod
    async def __anext__(self) -> str:
        raise NotImplementedError
