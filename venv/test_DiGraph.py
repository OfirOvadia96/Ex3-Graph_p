import unittest
from DiGraph import DiGraph
from Node import Node

class test_DiGraph(unittest.TestCase):

    def test_v_size(self):
        graph = DiGraph()
        self.assertEqual(graph.node_size, 0)

        for i in range(0,6):
            graph.add_node(i)

        self.assertEqual(graph.node_size , 6)

        graph.remove_node(1)
        self.assertEqual(graph.node_size , 5)

        graph.remove_node(100)
        self.assertEqual(graph.node_size, 5)


    def test_e_size(self):
        graph = DiGraph()
        self.assertEqual(graph.edge_size, 0)

        for i in range(0,3):
            graph.add_node(i)

        graph.add_edge(0 , 1 , 1)
        self.assertEqual(graph.edge_size, 1)

        graph.add_edge(1 , 2 , 3)
        self.assertEqual(graph.edge_size, 2)

        graph.add_edge(1 , 2 ,1)
        self.assertEqual(graph.edge_size, 2)

        graph.remove_edge(1 , 2)
        self.assertEqual(graph.edge_size, 1)

        graph.remove_edge(1, 2)
        self.assertEqual(graph.edge_size, 1)



    def test_get_mc(self):
        graph = DiGraph()
        self.assertEqual(graph.get_mc() , 0)
        for i in range(1,7):
            graph.add_node(i)

        self.assertEqual(graph.get_mc(), 6)

        for i in range(1,7):
            graph.remove_node(i)

        self.assertEqual(graph.get_mc() , 12)

        for i in range(1,7):
            graph.add_node(i)

        graph.add_edge(1 ,2 ,1)
        graph.add_edge(3 ,4 ,2)
        graph.add_edge(5 ,6 ,3)
        self.assertEqual(graph.get_mc(), 21)

        graph.add_edge(1 ,2 ,1)
        self.assertEqual(graph.get_mc(), 21)

        graph.add_edge(1, 3, 1)
        graph.add_edge(1, 4, 2)
        graph.add_edge(1, 5, 3)
        graph.add_edge(1, 6, 1)
        graph.remove_node(1)
        self.assertEqual(graph.get_mc(), 26)

        graph1 = DiGraph()
        for i in range(1,5):
            graph1.add_node(i)

        graph1.add_edge(2 ,1 ,1)
        graph1.add_edge(3, 1, 1)
        graph1.add_edge(4, 1, 1)
        n1 = graph1.TheGraph[1]
        graph1.remove_node(n1.id)
        self.assertEqual(graph1.get_mc(), 8)


    def test_add_edge(self):
        graph = DiGraph()
        for i in range(1,6):
            graph.add_node(i)

        graph.add_edge(1 ,2 ,1)
        graph.add_edge(1 ,3 ,1)
        graph.add_edge(2 ,3 ,1)
        graph.add_edge(3 ,4 ,1)
        self.assertTrue(graph.add_edge(4 ,5 ,1))

        self.assertEqual(graph.edge_size ,5)

        graph.add_edge(2 ,1 ,2)
        graph.add_edge(3 ,1 ,2)
        self.assertEqual(graph.edge_size, 7)

        graph.add_edge(1 ,3 ,1)
        self.assertEqual(graph.edge_size, 7)

        self.assertFalse(graph.add_edge(1, 100, 1))

        self.assertFalse( graph.add_edge(1 ,3 ,-1))


    def test_add_node(self):
        graph = DiGraph()
        for i in range(1,7):
            graph.add_node(i)

        self.assertEqual(graph.node_size ,6)

        graph.add_node(1)
        graph.add_node(2)
        self.assertEqual(graph.node_size, 6)

        self.assertFalse(graph.add_node(5))


    def test_remove_node(self):
        graph = DiGraph()
        for i in range(1,7):
            graph.add_node(i)

        graph.remove_node(1)
        self.assertEqual(graph.node_size, 5)

        graph.remove_node(2)
        self.assertEqual(graph.node_size, 4)

        graph.remove_node(100)
        self.assertEqual(graph.node_size, 4)


    def test_remove_edge(self):
        graph = DiGraph()
        for i in range(1,6):
            graph.add_node(i)

        graph.add_edge(1 ,2 ,1)
        graph.add_edge(1, 3, 1)
        graph.add_edge(1, 4, 1)
        graph.add_edge(1, 5, 1)
        graph.add_edge(5, 1, 1)

        self.assertEqual(graph.edge_size ,5)

        self.assertFalse(graph.remove_edge(1 ,100))

        self.assertTrue(graph.remove_edge(1 ,2))

        self.assertTrue(graph.remove_edge(1 ,5))

        self.assertEqual(graph.edge_size, 3)


    def test_all_in_edges_of_node(self):
        graph = DiGraph()
        for i in range(1, 10):
            graph.add_node(i)

        graph.add_edge(1, 2, 2)
        graph.add_edge(2, 1, 5)
        graph.add_edge(2, 3, 1)
        graph.add_edge(4, 2, 7.5)
        expected_dict = {1: 2, 4: 7.5}
        self.assertEqual(graph.all_in_edges_of_node(2), expected_dict)

        self.assertEqual(graph.all_in_edges_of_node(7), {})


    def test_all_out_edges_of_node(self):
        graph = DiGraph()
        for i in range(1, 10):
            graph.add_node(i)

        graph.add_edge(1, 2, 2)
        graph.add_edge(2, 1, 5)
        graph.add_edge(2, 3, 1)
        graph.add_edge(4, 2, 7.5)
        expected_dict = {1: 5, 3: 1}
        self.assertEqual(graph.all_out_edges_of_node(2), expected_dict)

        self.assertEqual(graph.all_out_edges_of_node(3), {})


    def test_get_all_v(self):
        graph = DiGraph()
        expected_dict = {}

        for i in range(1, 10):
            graph.add_node(i)
            expected_dict[i] = graph.TheGraph.get(i)

        self.assertEqual(graph.get_all_v(), expected_dict)


if __name__ == '__main__':
    unittest.main()
