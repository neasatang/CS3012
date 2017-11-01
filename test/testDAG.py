from directedAcyclicGraph import DAG
import unittest

directAcyclicGraph = None

class MyTestCase(unittest.TestCase):

    # test for add one node
    def test_add_node(self):
        global directAcyclicGraph
        directAcyclicGraph = DAG()
        directAcyclicGraph.add_node('A')
        #directAcyclicGraph.print_graph(directAcyclicGraph.graph)
        self.assertTrue(directAcyclicGraph.graph == {'A': []})

    #test for duplicate of same node
    def test_add_node3(self):
        self.assertFalse(directAcyclicGraph.add_node('A'))

    #test for a non-existent node
    def test_add_node2(self):
        directAcyclicGraph = DAG()
        directAcyclicGraph.add_node('B')
        self.assertFalse(directAcyclicGraph.graph == {'A': []})

    #test for DFS_Wrapper and DFS i.e. this returns false if contains cycles in graph
    def test_DAG(self):
        directAcyclicGraph = DAG()
        directAcyclicGraph.add_node('B')
        directAcyclicGraph.add_node('C')
        directAcyclicGraph.add_edge('B','C')
        directAcyclicGraph.add_node('D')
        directAcyclicGraph.add_node('E')
        directAcyclicGraph.add_edge('C', 'D')
        directAcyclicGraph.add_edge('D', 'B')
        #print(directAcyclicGraph)
        self.assertFalse(directAcyclicGraph.DFSWrapper(directAcyclicGraph.graph))

    # test for DFS_Wrapper and DFS i.e. this returns true if contains no cycles in graph
    def test_DAG2(self):
        directAcyclicGraph = DAG()
        directAcyclicGraph.add_node('B')
        directAcyclicGraph.add_node('C')
        directAcyclicGraph.add_edge('B','C')
        self.assertTrue(directAcyclicGraph)


    #### test for LCA_DFS_Wrapper and LCA_DFS
    # test for LCA between two nodes in a graph
    def test_LCA(self):
        directAcyclicGraph = DAG()
        directAcyclicGraph.add_node('A')
        directAcyclicGraph.add_node('B')
        directAcyclicGraph.add_node('C')
        directAcyclicGraph.add_node('D')
        directAcyclicGraph.add_node('E')
        directAcyclicGraph.add_node('F')
        directAcyclicGraph.add_node('G')
        directAcyclicGraph.add_node('H')
        directAcyclicGraph.add_edge('A','B')
        directAcyclicGraph.add_edge('A', 'C')
        directAcyclicGraph.add_edge('A', 'D')
        directAcyclicGraph.add_edge('B', 'C')
        directAcyclicGraph.add_edge('C', 'E')
        directAcyclicGraph.add_edge('B', 'F')
        directAcyclicGraph.add_edge('E', 'F')
        directAcyclicGraph.add_edge('F', 'H')
        directAcyclicGraph.add_edge('D', 'G')
        directAcyclicGraph.LCA_DFS_Wrapper(directAcyclicGraph.graph, 'H','E')
        self.assertTrue(directAcyclicGraph.LCA_DFS_Wrapper(directAcyclicGraph.graph, 'H','E')== 'E')

    # test for LCA between two nodes in graph
    def test_LCA2(self):
        directAcyclicGraph = DAG()
        directAcyclicGraph.add_node('A')
        directAcyclicGraph.add_node('B')
        directAcyclicGraph.add_node('C')
        directAcyclicGraph.add_node('D')
        directAcyclicGraph.add_node('E')
        directAcyclicGraph.add_node('F')
        directAcyclicGraph.add_node('G')
        directAcyclicGraph.add_node('H')
        directAcyclicGraph.add_edge('A', 'B')
        directAcyclicGraph.add_edge('A', 'C')
        directAcyclicGraph.add_edge('A', 'D')
        directAcyclicGraph.add_edge('B', 'C')
        directAcyclicGraph.add_edge('C', 'E')
        directAcyclicGraph.add_edge('B', 'F')
        directAcyclicGraph.add_edge('E', 'F')
        directAcyclicGraph.add_edge('F', 'H')
        directAcyclicGraph.add_edge('D', 'G')
        self.assertTrue(directAcyclicGraph.LCA_DFS_Wrapper(directAcyclicGraph.graph, 'H', 'G') == 'A')

    # test for LCA of a node and a non-node in graph
    def test_LCA3(self):
        directAcyclicGraph = DAG()
        directAcyclicGraph.add_node('A')
        directAcyclicGraph.add_node('B')
        directAcyclicGraph.add_edge('A','B')
        self.assertTrue(directAcyclicGraph.LCA_DFS_Wrapper(directAcyclicGraph.graph, 'A', 'G') == None)

    # test for LCA of an empty graph
    def test_LCA4(self):
        directAcyclicGraph = DAG()
        self.assertTrue(directAcyclicGraph.LCA_DFS_Wrapper(directAcyclicGraph.graph, None, None) == None)


if __name__ == '__main__':
    unittest.main()
