# Ex3-Graph_p

<h2>Fourth Assignment in the Object Oriented Programming Course - Graph:</h2>

**This task deals with building a graph data structure
Program interfaces:**

* GraphInterface
* GraphAlgoInterface
* Program classes

<h3> Node:</h3>

**This class represents a node**

***Department capabilities:***

* Building a node that holds two dictionaries that describe the edges that enter the same node and the edeges that are sent from it to other nodes
(In other words his neighbors)

* Comparison of nodes for other functions located in the other classes

* reper that returns the Node object as a dictionary



<h3> DiGraph: </h3>

**A class that implements the GraphInterface interface and displays the graph itself and of course imports the Node class that displays the nodes on the graph**

***Department capabilities:***

* Receiving a node is desirable according to its value

* Know how many nodes are in the graph

* Know the amount of edges in the class

* Know how many changes have been made to the graph

* Add a node to a graph

* Add an edge to the graph

* Deletion a node from the graph

* Deletion an edge from the graph

* Comparison of graphs

* Graph printing

* Return all nodes in the graph as a dictionary

* Returns all edges that enter a particular node in the graph as a dictionary

* Returns all edges sent to the various nodes from a particular node in the graph as a dictionary


<h3> GraphAlgo: </h3>

**A class that implements the GraphAlgoInterface interface, this class is based on the DiGraph class and in fact it is a class that implements additional algorithms and additional capabilities to the graph**

***Department capabilities:***

* Return the shortest route between intersections to each selected intersection

* Returns a list of nodes belonging to a binding component

* Returns a list that contains lists of all the binding components in the graph

* DijkstraAlgorithm function, - a graph scanning algorithm that analyzes the graph and updates all the information in it , helps solve the problem of the shortest path between two vertices contained in the graph.


<h4>The tests of the classes: </h4>

* test_DiGraph

* test_GraphAlgo
