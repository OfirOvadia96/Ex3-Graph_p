from GraphInterface import GraphInterface
from Node import Node


class DiGraph(GraphInterface):
    """
    This calss present directed and weighted graph
    """

    def __init__(self, NodeSize: int = 0, EdgeSize: int = 0 , Mc: int = 0):
        """
        constructor
        :param NodeSize:
        :param EdgeSize:
        :param Mc:
        """
        self.mc = Mc
        self.node_size = NodeSize
        self.edge_size = EdgeSize
        self.TheGraph = {}  # (Node_id :int , Node :object Node)


    def getNode(self, id: int) -> Node:
        """ 
        :param id: 
        :return: Node object of this id 
        """""
        if id in self.TheGraph:
            return self.TheGraph.get(id)
        else:
            return None


    def v_size(self) -> int:
        """
        :return: Amount of nodes in the graph
        """
        return self.node_size


    def e_size(self) -> int:
        """
        :return: Amount of edges in the graph
        """
        return self.edge_size


    def get_all_v(self) -> dict:
        """
        :return: dictionary of all the nodes in the graph
        """
        return self.TheGraph


    def all_in_edges_of_node(self, id1: int) -> dict:
        """
        :param id1:
        :return:  a dictionary of all the nodes connected into node_id
        """
        if id1 in self.TheGraph:
            return self.getNode(id1).edges_in


    def all_out_edges_of_node(self, id1: int) -> dict:
        """
        :param id1:
        :return: a dictionary of all the nodes connected from node_id
        """
        if id1 in self.TheGraph:
            return self.getNode(id1).edges_out


    def get_mc(self) -> int:
        """
        :return: the number of changes made to the graph
        """
        return self.mc


    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        Adds an edge to the graph.
        :param id1: The start node of the edge
        :param id2: The end node of the edge
        :param weight: The weight of the edge
        :return: True if the edge was added successfully, False if not
        """
        if id1 in self.TheGraph and id2 in self.TheGraph and id1 != id2 and weight > 0:
            n1 = self.getNode(id1)
            n2 = self.getNode(id2)
            if id2 in n1.edges_out:
                return False
            else:
                n1.edges_out[id2] = weight
                n2.edges_in[id1] = weight

                self.edge_size  += 1
                self.mc += 1
                return True
        else:
            return False


    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        Adds a node to the graph.
        :param node_id: the node id
        :param pos: The position of the node
        :return: True if the node was added successfully , False if not
        """
        if node_id in self.TheGraph:
            return False
        else:
            n1 = Node(node_id, tuple)
            self.TheGraph[node_id] = n1

            self.node_size += 1
            self.mc += 1
            return True


    def remove_node(self, node_id: int) -> bool:
        """
        Remove node from the graph.
        :param node_id: The node ID
        :return:True if the node was removed successfully , False if not
        """
        if node_id in self.TheGraph:
            n1 = self.TheGraph[node_id]
            for key in self.TheGraph: #Delete all the edges that enter the same node
                n2 = self.TheGraph[key]
                if n2.id != node_id and node_id in n2.edges_out:
                    self.remove_edge(n2.id , n1.id)
                    self.mc -=1

            self.TheGraph.pop(node_id) #Removing the node from the graph
            self.mc += 1
            self.node_size -= 1
            return True
        else:
            return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        Removes an edge from the graph.
        :param node_id1: The start node of the edge
        :param node_id2: The end node of the edge
        :return: True if the edge was removed successfully, False if not
        """
        if node_id1 in self.TheGraph and node_id2 in self.TheGraph and node_id1 != node_id2:

            n1 = self.getNode(node_id1)
            n2 = self.getNode(node_id2)
            if node_id1 in n2.edges_in or node_id2 in n1.edges_out:

                del n1.edges_out[node_id2]
                del n2.edges_in[node_id1]

                self.edge_size  -= 1
                self.mc += 1
                return True
            else:
                return False
        else:
            return False

    def __str__(self):
        return "Graph:" + "|V|=" + str(self.node_size) + "|E|=" + str(self.edge_size )

    def __repr__(self):
        return str(self.__dict__)


    def __eq__(self, other):
        if isinstance(other, self.__class__) is False:
            return False
        if self.v_size() != other.v_size() or self.e_size() != other.e_size():
            return False
        return self.get_all_v() == other.get_all_v()


    def repr_json(self):
        return self.__dict__

    def load_from_json(self, json_dict):
        self.nodeSize = json_dict["Nodes"]
        self.edgeSize = json_dict["Edges"]
        self.mc = json_dict["mc"]
        self.graphDict = {k: Node(**v) for (k, v) in json_dict["graphDict"].items()}
