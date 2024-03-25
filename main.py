import random
import numpy as np


class AdjNode:
    def __init__(self, weight: int, boolean_tag: bool) -> None:
        self.weight: int = weight
        self.boolean_tag: bool = boolean_tag

    def __repr__(self) -> str:
        return f"{self.weight}"


def T(G: list[list[AdjNode]]) -> list[list[AdjNode]]:
    return [list(row) for row in zip(*G)]


def add(G: list[list[AdjNode]], G_T: list[list[AdjNode]]) -> list[list[AdjNode]]:
    return [
        [
            AdjNode(
                G[i][j].weight + G_T[i][j].weight,
                G[i][j].boolean_tag or G_T[i][j].boolean_tag,
            )
            for j in range(len(G[0]))
        ]
        for i in range(len(G))
    ]
