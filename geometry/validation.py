from abc import ABC, abstractmethod
from typing import Any


class FigureValidation(ABC):

    def __init__(self, *args: Any, **kwargs: Any):
        pass

    @abstractmethod
    def validate(self) -> None:
        raise NotImplementedError()
