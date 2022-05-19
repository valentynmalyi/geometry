from typing import Any, Type

from .validation import FigureValidation


class Figure:
    validation_class: Type[FigureValidation]

    def __init__(self, *args: Any, **kwargs: Any):
        self.validation_class(*args, **kwargs).validate()
