from src.base import Circle

class CircleWrapper:

    def __init__(self, circle:Circle) -> None:
        self.circle = circle

    def predict(self, x: float, y: float) -> bool:
        return self.circle.predict(x, y)