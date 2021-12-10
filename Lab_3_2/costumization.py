from __future__ import annotations

from abc import ABC


class Customization(ABC):
    def __init__(self, extraMilk: float, sugar: float, mugSize: float):
        self.milk = extraMilk
        self.sugar = sugar
        self.size = mugSize
