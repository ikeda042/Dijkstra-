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

    def search_path(self, startNode: str, endNode: str):

        # 最短距離を無限大に初期化
        for i in self.nodes.keys():
            self.nodes[i].d = float("inf")

        queue: list[str] = [startNode]
        # currNodeを初期化
        currNode: str = queue[0]
        # currNodeの距離を初期化
        self.nodes[currNode].set_d(0)
        # 初期ノードのprevNodeを初期化
        self.nodes[currNode].prev_node = None

        while len(queue) > 0:
            currNode = queue.pop(0)
            adjs = self.nodes[currNode].adj
            for i in adjs.keys():
                tmp_d: float = self.nodes[currNode].d + self.nodes[currNode].adj[i]
                if self.nodes[i].d > tmp_d:
                    # スタートノードからの最短到達距離を更新
                    self.nodes[i].set_d(int(tmp_d))
                    self.nodes[i].prev_node = self.nodes[currNode]
                    self.nodes[i].set_explored(True)
                    queue.append(i)
        cNode: Node = self.nodes[endNode]

        # Backtrack
        s: list[str] = [endNode]
        while cNode.prev_node != None:
            cNode = cNode.prev_node
            s.append(cNode.name)

        return [s[::-1], self.nodes[endNode].d]
