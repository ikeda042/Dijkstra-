import random
import numpy as np


class Node:
    def __init__(self, weight: int, boolean_tag: bool) -> None:
        self.weight: int = weight
        self.boolean_tag: bool = boolean_tag

    def __repr__(self) -> str:
        return f"{self.weight}"


def T(G: list[list[Node]]) -> list[list[Node]]:
    return [list(row) for row in zip(*G)]
