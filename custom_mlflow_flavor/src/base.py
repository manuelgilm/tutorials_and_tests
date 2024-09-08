# This file contains the Circle class that is used to predict if a point is inside a circle.
import pickle
from pathlib import Path
from typing import Union


class Circle:

    def __init__(self, radius: float, x: float, y: float):
        self.radius = radius
        self.x = x
        self.y = y

    def predict(self, x: float, y: float) -> bool:
        """
        Predict if the point (x, y) is inside the circle.

        :param x: float
        :param y: float
        :return: bool
        """
        return self._evaluate_point(x, y)

    def _evaluate_point(self, x: float, y: float) -> bool:
        """
        Evaluate if the point (x, y) is inside the circle.

        :param x: float
        :param y: float
        :return: bool
        """

        return (x - self.x) ** 2 + (y - self.y) ** 2 <= self.radius**2

    def save(self, path: Union[str, Path]) -> None:
        """
        Save the circle to a file.

        :param path: str
        :return: None
        """
        if isinstance(path, str):
            path = Path(path)

        with open(path, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def load(cls, path: Union[str, Path]) -> "Circle":
        """
        Load the circle from a file.

        :param path: str
        :return: Circle
        """
        with open(path, "rb") as file:
            return pickle.load(file)
