import unittest
from src.DiGraph import DiGraph


class TestStringMethods(unittest.TestCase):

    def test_add_node(self):
        g0 = DiGraph()
        for i in range(0, 20):
            g0.add_node(i)
        self.assertEqual(20, g0.v_size())
        self.assertEqual(20, g0.get_mc())
        for i in range(50, 70):
            g0.add_node(i)
        self.assertEqual(40, g0.v_size())
        self.assertEqual(40, g0.get_mc())
        g0.remove_node(3)
        self.assertEqual(39, g0.v_size())
        self.assertEqual(41, g0.get_mc())
        g0.add_node(100)
        self.assertEqual(40, g0.v_size())
        self.assertEqual(42, g0.get_mc())

    def test_add_edge(self):
        g0 = DiGraph()
        for i in range(0, 20):
            g0.add_node(i)
        for i in range(0, 5):
            g0.add_edge(i, i+1, 5)
        self.assertEqual(g0.get_mc(), 25)
        self.assertEqual(g0.e_size(), 5)
        self.assertFalse(g0.add_edge(1, 2, 3))
        g0.remove_node(2)
        self.assertEqual(g0.e_size(), 3)
        self.assertEqual(g0.get_mc(), 28)

    def test_remove_node(self):
        g0 = DiGraph()
        for i in range(0, 50):
            g0.add_node(i)
        g0.remove_node(47)
        self.assertFalse(47 in g0.graph)
        self.assertFalse(g0.remove_node(200))
        self.assertEqual(g0.get_mc(), 51)

    def test_v_size(self):
        g0 = DiGraph()
        for i in range(0, 50):
            g0.add_node(i)
        self.assertEqual(50, g0.v_size())
        for i in range(0, 20):
            g0.remove_node(i)
        self.assertEqual(30, g0.v_size())
        self.assertEqual(g0.get_mc(), 70)

    def test_e_size(self):
        g0 = DiGraph()
        for i in range(0, 50):
            g0.add_node(i)
        for i in range(0, 20):
            g0.add_edge(i, i+1, 5)
        self.assertEqual(20, g0.e_size())

    def test_get_all_v(self):
        g0 = DiGraph()
        counter = 0
        for i in range(0, 50):
            g0.add_node(i)
        for x in g0.get_all_v():
            counter += 1
            self.assertTrue(x in g0.graph)
        self.assertEqual(counter, g0.v_size())

    def test_all_in_edges_of_node(self):
        g0 = DiGraph()
        for i in range(0, 50):
            g0.add_node(i)
        for i in range(0, 20):
            g0.add_edge(i, i + 1, 5)
        for x in g0.all_in_edges_of_node(18):
            self.assertTrue(18 in g0.all_out_edges_of_node(x))

    def test_all_out_edges_of_node(self):
        g0 = DiGraph()
        for i in range(0, 50):
            g0.add_node(i)
        for i in range(0, 20):
            g0.add_edge(i, i + 1, 5)
        for x in g0.all_out_edges_of_node(18):
            self.assertTrue(18 in g0.all_in_edges_of_node(x))

    def test_mc(self):
        g0 = DiGraph()
        for i in range(0, 10):
            g0.add_node(i)
        g0.add_edge(4, 3, 1)
        g0.add_edge(4, 2, 1)
        g0.add_edge(2, 4, 1)
        g0.add_edge(1, 2, 1)
        g0.add_edge(5, 3, 1)
        g0.add_edge(4, 5, 1)
        self.assertEqual(16, g0.get_mc())
        g0.add_edge(4, 5, 1)  # already exist
        self.assertEqual(16, g0.get_mc())
        g0.add_node(3)  # already exist
        self.assertEqual(16, g0.get_mc())
        g0.remove_edge(2, 4)
        self.assertEqual(17, g0.get_mc())
        g0.remove_edge(2, 4)  # removing twice
        self.assertEqual(17, g0.get_mc())
        g0.remove_node(2)
        self.assertEqual(20, g0.get_mc())
        g0.remove_node(2)  # adding twice
        self.assertEqual(20, g0.get_mc())

    def test_get_weight(self):
        g0 = DiGraph()
        for i in range(0, 50):
            g0.add_node(i)
        g0.add_edge(4, 3, 30)
        g0.add_edge(4, 3, 0.5)  # should not update
        self.assertFalse(g0.add_edge(4, 4, 1))
        self.assertEqual(30, g0.connectionsSrc.get(4, {}).get(3))

