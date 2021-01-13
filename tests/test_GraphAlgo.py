from unittest import TestCase
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


class TestGraphAlgo(TestCase):
    def test_shortest_path(self):
        g = DiGraph()
        ga = GraphAlgo(g)
        for x in range(5):
            g.add_node(x)
        g.add_edge(0, 1, 5)
        g.add_edge(0, 2, 2)
        g.add_edge(1, 3, 8)
        g.add_edge(2, 3, 1)
        g.add_edge(3, 2, 1)
        g.add_edge(3, 4, 3)
        l1 = ga.shortest_path(3, 3)[1]
        self.assertTrue(len(l1) == 1 and 3 in l1)
        l2 = ga.shortest_path(0, 4)[1]
        self.assertTrue(len(l2) == 4)
        self.assertTrue(l2 == [0, 2, 3, 4])

    def test_connected_component(self):
        g = DiGraph()
        ga = GraphAlgo(g)
        for x in range(5):
            g.add_node(x)
        g.add_edge(0, 1, 5)
        g.add_edge(0, 2, 2)
        g.add_edge(1, 3, 8)
        g.add_edge(2, 3, 1)
        g.add_edge(3, 2, 1)
        g.add_edge(3, 4, 3)
        l1 = ga.connected_component(0)
        self.assertTrue(l1 == [0])
        l2 = ga.connected_component(3)
        self.assertTrue(2 in l2)
        self.assertTrue(3 in l2)

    def test_connected_components(self):
        g = DiGraph()
        ga = GraphAlgo(g)
        for x in range(5):
            g.add_node(x)
        g.add_edge(0, 1, 5)
        g.add_edge(0, 2, 2)
        g.add_edge(1, 3, 8)
        g.add_edge(2, 3, 1)
        g.add_edge(3, 2, 1)
        g.add_edge(3, 4, 3)
        all_scc = ga.connected_components()
        print(all_scc)

    def test_save_to_json(self):
        g = DiGraph()
        ga = GraphAlgo(g)
        for x in range(5):
            g.add_node(x)
        g.add_edge(0, 1, 5.0)
        g.add_edge(0, 2, 2)
        g.add_edge(1, 3, 8.6)
        g.add_edge(2, 3, 1)
        g.add_edge(3, 2, 1)
        g.add_edge(3, 4, 3.6)
        self.assertTrue(ga.save_to_json("C:\\Users\\koren\\PycharmProjects\\Ex3\\src\\graph.json"))

    def test_load_from_json(self):
        g = DiGraph()
        g2 = DiGraph()
        g_save = GraphAlgo(g)
        g_load = GraphAlgo(g2)
        for x in range(5):
            g.add_node(x)
        g.add_edge(0, 1, 5.0)
        g.add_edge(0, 2, 2)
        g.add_edge(1, 3, 8.6)
        g.add_edge(2, 3, 1)
        g.add_edge(3, 2, 1)
        g.add_edge(3, 4, 3.6)
        self.assertTrue(g_save.save_to_json("C:\\Users\\koren\\PycharmProjects\\Ex3\\src\\graph.json"))
        self.assertTrue(g_load.load_from_json("C:\\Users\\koren\\PycharmProjects\\Ex3\\src\\graph.json"))
        self.assertTrue(g_load.myGraph.numNodes == g_save.myGraph.numNodes)
        self.assertTrue(g_load.myGraph.numEdges == g_save.myGraph.numEdges)
        for x in g_save.myGraph.graph:
            self.assertTrue(x in g_load.myGraph.graph)
            self.assertTrue(g_save.myGraph.all_out_edges_of_node(x) == g_load.
                            myGraph.all_out_edges_of_node(x))
