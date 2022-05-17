from abc import ABC, abstractmethod


class FigureValidation(ABC):

    @abstractmethod
    def validate(self) -> None:
        raise NotImplementedError()
