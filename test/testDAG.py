from directedAcyclicGraph import DAG
import unittest

directAcyclicGraph = None

class MyTestCase(unittest.TestCase):

    def test_add_node(self):
        global directAcyclicGraph
        directAcyclicGraph = DAG()
        directAcyclicGraph.add_node('A')
        #directAcyclicGraph.print_graph(directAcyclicGraph.graph)
        self.assertTrue(directAcyclicGraph.graph == {'A': []})

    def test_add_node3(self):
        self.assertFalse(directAcyclicGraph.add_node('A'))

    def test_add_node2(self):
        directAcyclicGraph = DAG()
        directAcyclicGraph.add_node('B')
        self.assertFalse(directAcyclicGraph.graph == {'A': []})

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

    def test_DAG2(self):
        directAcyclicGraph = DAG()
        directAcyclicGraph.add_node('B')
        directAcyclicGraph.add_node('C')
        directAcyclicGraph.add_edge('B','C')
        self.assertTrue(directAcyclicGraph)


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
        #directAcyclicGraph.print_graph(directAcyclicGraph.graph)
        directAcyclicGraph.LCA_DFS_Wrapper(directAcyclicGraph.graph, 'H','E')

        directAcyclicGraph.LCA_DFS_Wrapper(directAcyclicGraph.graph, 'H', 'G')




if __name__ == '__main__':
    unittest.main()
