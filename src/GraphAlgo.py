import json
import queue
from random import uniform
import numpy as np
from matplotlib.patches import ConnectionPatch
import matplotlib.pyplot as window
from src.DiGraph import DiGraph


class GraphAlgo:

    def __init__(self, g: DiGraph = None):
        if g is None:
            g = DiGraph()
        self.myGraph = g

    def get_graph(self) -> DiGraph:
        return self.myGraph

    """
    :return: the directed graph on which the algorithm works on.
    """

    def save_to_json(self, file_name: str):
        g = self.myGraph
        json_dic = {}
        Nodes = []
        Edges = []
        for x in g.graph:
            temp_dic = {"id": x, "pos": ",".join(map(str, g.get_node(x).get_pos()))}
            Nodes.append(temp_dic)
        for x in g.connectionsSrc:
            for z in g.connectionsSrc.get(x, {}):
                temp_dic = {"src": x, "dest": z, "w": g.connectionsSrc.get(x, {}).get(z)}
                Edges.append(temp_dic)
        json_dic["Nodes"] = Nodes
        json_dic["Edges"] = Edges
        try:
            with open(file_name, 'w') as file:
                json.dump(json_dic, file)
                return True
        except IOError as error:
            print(error)
            return False

    """
    Saves the graph in JSON format to a file
    @param file_name: The path to the out file
    @return: True if the save was successful, False o.w.
    """

    def load_from_json(self, file_name: str) -> bool:
        try:
            with open(file_name) as json_file:
                data = json.load(json_file)
            workGraph = self.myGraph
            workGraph.graph.clear()
            for p in data["Nodes"]:
                workGraph.add_node(p["id"])
                if "pos" in p:
                    new_pos = tuple(map(float, p["pos"].split(',')))
                    workGraph.get_node(p["id"]).set_pos(new_pos)
            for p in data["Edges"]:
                workGraph.add_edge(p["src"], p["dest"], p["w"])
            return True
        except IOError as error:
            print(error)
            return False

    """
    Loads a graph from a json file.
    @param file_name: The path to the json file
    @returns True if the loading was successful, False o.w.
    """

    def shortest_path(self, id1: int, id2: int):
        path = []
        if id1 in self.myGraph.graph and id2 in self.myGraph.graph:
            if id1 == id2:
                path.append(id1)
                return 0, path
            parent = {}  # keys
            visited = set()  # keys only
            blacklist = set()  # keys only
            neighbors = queue.PriorityQueue()
            neighbors.put((self.myGraph.get_node(id1).get_weight(), id1))
            for x in self.myGraph.graph:
                self.myGraph.get_node(x).set_weight(0)
            if len(self.myGraph.all_in_edges_of_node(id2)) == 0:
                return float('inf'), []
            while not neighbors.empty() and id2 not in blacklist:
                srcNodeId = neighbors.get()[1]
                blacklist.add(srcNodeId)
                for x in self.myGraph.connectionsSrc.get(srcNodeId):
                    if x not in visited:
                        self.myGraph.get_node(x).set_weight(
                            self.myGraph.get_node(srcNodeId).get_weight() + self.myGraph.
                            connectionsSrc.get(srcNodeId, {}).get(x))
                        parent[x] = srcNodeId
                        visited.add(x)
                        neighbors.put((self.myGraph.get_node(x).get_weight(), x))
                    elif self.myGraph.connectionsSrc.get(srcNodeId, {}).get(x) + self.myGraph.get_node(srcNodeId) \
                            .get_weight() < self.myGraph.get_node(x).get_weight():
                        self.myGraph.get_node(x).set_weight(
                            self.myGraph.get_node(srcNodeId).get_weight() + self.myGraph.
                            connectionsSrc.get(srcNodeId, {}).get(x))
                        parent[x] = srcNodeId
            if id2 in parent:
                stack = []
                tempID = id2
                while tempID != id1:
                    stack.append(tempID)
                    tempID = parent.get(tempID)
                stack.append(id1)
                while len(stack) != 0:
                    path.append(stack.pop())
                return self.myGraph.get_node(id2).get_weight(), path
            else:
                return float('inf'), []
        return float('inf'), []

    """
    Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
    @param id1: The start node id
    @param id2: The end node id
    @return: The distance of the path, a list of the nodes ids that the path goes through
    Notes:
    If there is no path between id1 and id2, or one of them dose not exist the function returns (float('inf'),[])
    """

    def connected_component(self, id1: int) -> list:
        if len(self.myGraph.graph) == 0 or id1 not in self.myGraph.graph:
            return []
        visited1 = set()  # keys
        neighbors1 = queue.Queue()  # keys
        neighbors1.put(id1)
        visited1.add(id1)
        if len(self.myGraph.all_out_edges_of_node(id1)) == 0 or len(self.myGraph.all_in_edges_of_node(id1)) == 0:
            return [id1]
        while not neighbors1.empty():
            temp = neighbors1.get()
            for x in self.myGraph.all_out_edges_of_node(temp):
                if x not in visited1:
                    visited1.add(x)
                    neighbors1.put(x)

        visited2 = set()  # keys
        neighbors2 = queue.Queue()  # keys
        neighbors2.put(id1)
        visited2.add(id1)
        while not neighbors2.empty():
            temp = neighbors2.get()
            for x in self.myGraph.all_in_edges_of_node(temp):
                if x not in visited2:
                    visited2.add(x)
                    neighbors2.put(x)
        return [x for x in visited1 if x in visited2]

    """
    Finds the Strongly Connected Component(SCC) that node id1 is a part of.
    @param id1: The node id
    @return: The list of nodes in the SCC

    Notes:
    If the graph is None or id1 is not in the graph, the function should return an empty list []
    """

    def connected_components(self):
        all_scc = []
        graph_nodes = set()
        for x in self.myGraph.graph:
            graph_nodes.add(x)  # add all the nodes_id to the set
        while len(graph_nodes) != 0:
            temp_list = self.connected_component(graph_nodes.pop())
            all_scc.append(temp_list)
            for x in temp_list:
                graph_nodes.discard(x)
        return all_scc

    """
    Finds all the Strongly Connected Component(SCC) in the graph.
    @return: The list all SCC

    Notes:
    If the graph is None the function should return an empty list []
    """

    def plot_graph(self):
        fig, ax = window.subplots()
        Nodes = self.myGraph.graph
        for i in Nodes:
            if self.myGraph.get_node(i).get_pos()[0] == 0 or self.myGraph.get_node(i).get_pos()[1] == 0:
                new_pos = uniform(35, 36), uniform(32, 33), 0
                self.myGraph.get_node(i).set_pos(new_pos)
            x, y, z = self.myGraph.get_node(i).get_pos()
            curr_node_pos = np.array([x, y])
            xyA = curr_node_pos
            ax.annotate(self.myGraph.get_node(i).get_id(), (x, y),
                        color='black',
                        fontsize=12)  # draw id
            for e in self.myGraph.all_out_edges_of_node(i):
                if self.myGraph.get_node(e).get_pos()[0] == 0 or self.myGraph.get_node(e).get_pos()[1] == 0:
                    new_pos = uniform(35, 36), uniform(32, 33), 0
                    self.myGraph.get_node(e).set_pos(new_pos)
                x, y, z = self.myGraph.get_node(e).get_pos()
                curr_node_pos = np.array([x, y])
                xyB = curr_node_pos
                con = ConnectionPatch(xyA, xyB, "data", "data",
                                      arrowstyle="-|>", shrinkA=6, shrinkB=6,
                                      mutation_scale=14, fc="yellow", color="blue")
                ax.plot([xyA[0], xyB[0]], [xyA[1], xyB[1]], "o", color='yellow', markersize=8, linewidth=10)
                ax.add_artist(con)

        window.show()

    """
    Plots the graph.
    If the nodes have a position, the nodes will be placed there.
    Otherwise, they will be placed in a random but elegant manner.
    @return: None
    """
