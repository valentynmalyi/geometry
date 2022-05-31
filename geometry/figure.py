from dataclasses import dataclass, field
from typing import Type

from .validation import FigureValidation


@dataclass()
class Figure:
    validation_class: Type[FigureValidation] = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self.validation_class(self).validate()
