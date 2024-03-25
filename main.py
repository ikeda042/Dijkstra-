import random
import numpy as np


class Node:
    def __init__(self, weight: int, is_barrier_free: bool) -> None:
        self.weight: int = weight
        self.is_barrier_free: bool = is_barrier_free

    def __repr__(self) -> str:
        return f"{self.weight}"


def T(G: list[list[Node]]) -> list[list[Node]]:
    return [list(row) for row in zip(*G)]
