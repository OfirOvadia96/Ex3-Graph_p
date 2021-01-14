from GraphInterface import GraphInterface
from GraphAlgoInterface import GraphAlgoInterface
from DiGraph import DiGraph
from Node import Node
import json
import queue
from math import inf
import matplotlib.pyplot as plt
import random
from typing import List



class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'repr_json'):
            return obj.repr_json()
        else:
            return json.JSONEncoder.default(self, obj)


def reboot(self):
    """
    Initializes the nodes of a graph to the default form
    :param di_graph:

    """
    nodes_dic = self.get_all_v()
    for k in nodes_dic.keys():
        node = self.getNode(k)
        node.prev = None
        node.tag = False
        node.info = "white"
        node.weight = 0

def reversed_graph(graph):
    """
    A function that reverses the graph
    :param graph: The graph will be reversed
    :return: Returns the reverse graph
    """
    The_nodes = graph.get_all_v()
    neighbors = {}
    reverse = DiGraph()

    for j, n in The_nodes.items():
        reverse.add_node(j, n.location)
        neighbors[j] = graph.all_out_edges_of_node(j)

    for j, n in neighbors.items():
        for i, weight in n.items():
            reverse.add_edge(i, j, weight)

    reboot(reverse)

    return reverse


def dfs(id: int, graph: DiGraph) -> list:
    list_SCC = [id]
    keys = []
    keys.append(id)

    while list_SCC:
        node = list_SCC.pop()
        keysList = list(graph.all_out_edges_of_node(node).keys())

        for i in keysList:
            if not graph.getNode(i).tag:
                list_SCC.append(i)
                graph.getNode(i).tag = True
                keys.append(i)

    reboot(graph)
    return keys

class GraphAlgo(GraphAlgoInterface):

    """This class present Algorithm graph."""

    def __init__(self , graph = None):
        """
        constructor: create a graph
        :param graph: for deep copy constructor
        """
        if graph !=None:
            self.di_graph = graph
        else:
             self.di_graph = DiGraph()


    def get_graph(self) -> GraphInterface:
        return self.di_graph


    def load_from_json(self, file_name: str) -> bool:
        my_dict = dict()
        j_graph = DiGraph()
        try:
            with open(file_name, "r") as file:
                my_dict = json.load(file)
                nodes = my_dict["Nodes"]
                edges = my_dict["Edges"]

                for node_dict in nodes:
                    if len(node_dict) < 2:
                        j_graph.add_node(node_dict["id"])

                    else:
                        j_graph.add_node(node_dict["id"], node_dict["pos"])

                for edge_dict in edges:
                    j_graph.add_edge(edge_dict["src"], edge_dict["dest"], edge_dict["w"])

            self.graph = j_graph
            return True

        except IOError as e:
            print(e)
            return False


    def save_to_json(self, file_name: str) -> bool:
        nodes = []
        edges = []

        for node in self.get_graph().get_all_v().items():
            nodes_dict = dict()
            nodes_dict["id"] = node[1].id

            if len(node) > 1:
                nodes_dict["pos"] = node[1].location
            nodes.append(nodes_dict)
            node_edges = self.get_graph().all_out_edges_of_node(node[1].id)

            for edge in node_edges:
                edges_dict = dict()
                edges_dict["src"] = node[1].id
                edges_dict["dest"] = edge
                edges_dict["w"] = node_edges[edge]
                edges.append(edges_dict)

        ans = dict()
        ans["Nodes"] = nodes
        ans["Edges"] = edges

        try:
            with open(file_name, "w") as file:
                json.dump(ans, default=lambda m: m.__dict__, indent=4, fp=file)
                return True

        except IOError as e:
            print(e)
            return False


    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        :param id1: The start node id
        :param id2: The end node id
        :return: The distance of the path, a list of the nodes ids that the path goes through
        """
        lis = []
        if id1 not in self.di_graph.TheGraph or id2 not in self.di_graph.TheGraph or id1==id2:
            return inf,lis

        else:
            reboot(self.di_graph)
            self.dijkstra(id1)

            src = self.di_graph.getNode(id1)
            dest = self.di_graph.getNode(id2)
            dist = 0

            if dest.weight == 0:
                return inf, lis

            while not dest.__eq__(src):
                dist += dest.edges_in[dest.prev.id]
                lis.append(dest.id)
                dest = dest.prev

            lis.append(dest.id) # add the src
            lis.reverse()
            return (dist, lis)


    def connected_component(self, id1: int) -> list:
        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of.
        :param id1: The node id
        :return: The list of nodes in the SCC
        """
        list0 = dfs(id1, self.di_graph)
        if list is None:
            return []

        st1 = set(list0)
        reversed = reversed_graph(self.di_graph)
        list1 = dfs(id1, reversed)
        if list1 is None:
            return []

        st2 = set(list1)
        return list(st1 & st2)


    def connected_components(self):
        """
         Finds all the Strongly Connected Component(SCC) in the graph.
        :return:  The list all SCC
        """
        graph = self.get_graph()
        My_List = []
        for i in graph.get_all_v().keys():
            bol = False

            for x in My_List:
                if x.__contains__(i):
                    bol = True

            if not bol:
                Strongly_connected = self.connected_component(i)
                My_List.append(Strongly_connected)

        return My_List


    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        """
        XV = []
        YV = []
        graph = self.get_graph()
        sum = 10 * graph.v_size()
        nodes = graph.get_all_v().items()

        max_x = 0
        max_y = 0
        min_x = inf
        min_y = inf
        text = []
        for node in nodes:
            if node[1].location is None:
                self.__generate_locations()
            node_x = float(node[1].location.split(',')[0])
            node_y = float(node[1].location.split(',')[1])
            if node_x > max_x:
                max_x = node_x
            if node_y > max_y:
                max_y = node_y
            if node_x < min_x:
                min_x = node_x
            if node_y < min_y:
                min_y = node_y
        frame_y = max_y - min_y
        frame_x = max_x - min_x
        rad = 1 / 100 * frame_y
        for node in nodes:
            node_x = float(node[1].getPos().split(',')[0])
            node_y = float(node[1].getPos().split(',')[1])
            XV.append(node_x)
            YV.append(node_y)
            text.append([node_x + rad, node_y + rad, node[1].getKey()])
            for edge in graph.all_out_edges_of_node(node[0]):
                dest = graph.get_all_v()[edge]
                dest_x = float(dest.getPos().split(',')[0])
                dest_y = float(dest.getPos().split(',')[1])
                dx = dest_x - node_x
                dy = dest_y - node_y
                line_w = 0.0002 * frame_x

                if line_w > 0.2 * frame_y:
                    line_w = 0.2 * frame_y

                plt.arrow(node_x, node_y, dx, dy, width=line_w, length_includes_head=True, head_width=30 * line_w,
                          head_length=75 * line_w, color='k')

        for i in text:
            plt.text(i[0], i[1], i[2], color='b')

        plt.plot(XV, YV, 'o', color='r')
        plt.grid()
        plt.title("Graph")
        plt.ylabel("y")
        plt.xlabel("x")
        plt.show()


    def __generate_locations(self):
        sum = self.get_graph().v_size() + 10
        counter = 1
        graph = self.get_graph()
        for node in graph.get_all_v():
            x = counter / sum
            y = random.random()
            z = 0
            loc = str(x) + ',' + str(y) + ',' + str(z)
            dic = graph.get_all_v()[node].location = loc
            counter += 1


    def dijkstra(self, source:int):
        """
        Type of - dijkstra algorithm:
        :param source: ID of the node from which we will start running on the graph
        in the end: The connected nodes will be painted black, Their weight will show how close each node is to the source
        Each node will know who its previous node is ,  And the tag will show if we visited them .
        """

        p_queue = queue.PriorityQueue()
        node = self.di_graph.getNode(source)
        node.tag = True
        p_queue.put(node)

        while not p_queue.empty():
            current_node = p_queue.get()
            if current_node.info == "white":
                current_node.info = "grey"
                neighbors = self.di_graph.all_out_edges_of_node(current_node.id)

                for j in neighbors:
                    next_node = self.di_graph.getNode(j)

                    if next_node.weight == 0 and source != j:
                        next_node.weight = (current_node.weight + neighbors[j])
                        next_node.prev = current_node

                    else:
                        w = (neighbors[j] + current_node.weight)
                        if w < next_node.weight:
                            next_node.weight = w
                            next_node.prev = current_node

                    if next_node.tag is False:
                        next_node.tag = True
                        p_queue.put(next_node)
            current_node.info = "black"