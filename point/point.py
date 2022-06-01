from dataclasses import dataclass

from geometry import Figure

from .validations import PointValidation


@dataclass()
class Point(Figure):
    validation_class = PointValidation
    x: float
    y: float
