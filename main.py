import random
import numpy as np
from typing import cast


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


def generate_random_graph(R: int) -> np.ndarray:
    random.seed(10)
    weights_cs = [0] * 50 + [1] * 4 + [2] * 2 + [3] * 2 + [3] * 6 + [4] * 3 + [5] * 6
    p = [-1] * 5 + [1] * 21

    def get_weight():
        return random.choice(weights_cs) * random.choice(p)

    G: list[AdjNode] = [[AdjNode(0, False) for i in range(R)] for j in range(R)]
    for i in range(R):
        for j in range(R):
            if i == j or i < j:
                continue
            w = get_weight()
            cast(AdjNode, G[i][j]).weight = abs(w)
            cast(AdjNode, G[i][j]).boolean_tag = True if w > 0 else False
    return G


class Node:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.adj: dict[str, int] = {}
        self.d: float = float("inf")
        self.explored: bool = False
        self.prev_node: Node | None = None

    def __repr__(self) -> str:
        return self.name

    def set_explored(self, e: bool) -> None:
        self.explored = e

    def set_d(self, d: int) -> None:
        self.d = d


class PathFinder:
    def __init__(self, all_paths: dict[str, int], nodes_string: list[str]) -> None:
        self.nodes_string: list[str] = nodes_string
        self.nodes: dict[str, Node] = {i: Node(i) for i in nodes_string}
        for i in all_paths.keys():
            self.nodes[i.split("->")[0]].adj[i.split("->")[1]] = all_paths[i]
        print("+++++++++++++++++++++++++++++++++++")
        print(self.nodes)

    def search_path(self, start_node: str, end_node: str):

        # 最短距離を無限大に初期化
        for i in self.nodes.keys():
            self.nodes[i].d = float("inf")

        queue: list[str] = [start_node]
        # currNodeを初期化
        curr_node: str = queue[0]
        # currNodeの距離を初期化
        self.nodes[curr_node].set_d(0)
        # 初期ノードのprevNodeを初期化
        self.nodes[curr_node].prev_node = None

        while len(queue) > 0:
            curr_node = queue.pop(0)
            adjs = self.nodes[curr_node].adj
            for i in adjs.keys():
                tmp_d: float = self.nodes[curr_node].d + self.nodes[curr_node].adj[i]
                if self.nodes[i].d > tmp_d:
                    # スタートノードからの最短到達距離を更新
                    self.nodes[i].set_d(int(tmp_d))
                    self.nodes[i].prev_node = self.nodes[curr_node]
                    self.nodes[i].set_explored(True)
                    queue.append(i)

        c_node: Node = self.nodes[end_node]

        # Backtrack
        s: list[str] = [end_node]
        while c_node.prev_node != None:
            cNode = c_node.prev_node
            s.append(cNode.name)

        return [s[::-1], self.nodes[end_node].d]
