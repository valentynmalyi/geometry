from typing import Type

from .validation import FigureValidation


class Figure:
    validation: Type[FigureValidation]
