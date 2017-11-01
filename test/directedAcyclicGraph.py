import sys
class DAG(object):

    def print_graph(self, graph):
        print(graph)

    def print_node_list(self,list):
        print(list)

    # create empty set for nodes for the DAG
    def __init__(self):
        self.create_graph()

    # creates empty dict
    def create_graph(self):
        self.graph = {}

    # add node to set
    def add_node(self, node, graph=None):
        if not graph:
            graph = self.graph

        if node in graph:
            return False

        graph[node] = []

    # add edge to set
    def add_edge(self, ind_node, dep_node, graph=None):
        if not graph:
            graph = self.graph

        # if both nodes exist in the graph
        if ind_node in graph and dep_node in graph:
            graph[ind_node].append(dep_node)
        else:
            raise KeyError("One or both nodes do not exist")

    def DFS(self, node_list, graph, node):
        if not graph[node]:
            return True
        else:
            for child in graph[node]:
                if child not in node_list:
                    node_list.append(child)
                    if not self.DFS(node_list, graph, child):
                        return False
                    node_list.remove(child)
                else:
                    return False
            return True

    def DFSWrapper(self, graph):
        result = True
        for node in graph:
            if not self.DFS([node], graph, node):
                result = False
                break

        return result

    def LCA_DFS_Wrapper(self, graph, nodeA, nodeB):
        global node_A_list
        node_A_list = []
        global node_B_list
        node_B_list = []


        for node in graph:
            self.LCA_DFS([node], graph, node, 1, nodeA)
            self.LCA_DFS([node], graph, node, 2, nodeB)

        self.print_node_list(node_A_list)
        self.print_node_list(node_B_list)

        lowest_count = sys.maxsize
        for itemA in node_A_list:
            for itemB in node_B_list:
                count = 0
                for index, node1 in enumerate(reversed(itemA)):
                    count = index
                    for node2 in reversed(itemB):
                        if node1 == node2 and count < lowest_count:
                            LCANode = node2
                            lowest_count = count
                            break
                        count += 1
        print(LCANode)


    def LCA_DFS(self, node_list, graph, node, index, end_node):
        if node == end_node:
            if index == 1:
                node_A_list.append(node_list[:])
            elif index == 2:
                node_B_list.append(node_list[:])
            return True

        if not graph[node]:
            return True

        else:
            for child in graph[node]:
                if child not in node_list:
                    node_list.append(child)
                    if not self.LCA_DFS(node_list, graph, child, index, end_node):
                        return False
                    node_list.remove(child)
                else:
                    return False
            return True

