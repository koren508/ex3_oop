# Welcome to Ex3 Project – weighted & directed Graph. 

This project represents a weighted & directed graph.
the project is written with python.
the main idea of this project is to compare the same functions runtime between
java , python and networkX library(on python).

This project is based on Classes that we created such as:

node_data - represents the Vertex in the graph.
DiGraph - our graph that contains all the Vertex and Edges.
GraphAlgo - our graph which we operate our algorithms on.
note: class node_data is an inner class of DiGraph.

Each class offers us multiple functions to get information about the object.
we have several algorithms that we can operate on our graph such as:

isConnected() - return true if and only if there is a path from,
every Vertex to every other Vertex in the graph.
shortest_path(Vertex 1 , Vertex 2) - return the distance of the path *from* Vertex 1 *to* Vertex 2, and a list of the nodes ids that the path goes through.
connected_component(node id) - return a list with nodes ids that the Strongly Connected Component(SCC) that node id1 is a part of.
connected_components() - return a list of lists that containts all the Strongly Connected Component(SCC) in the graph.

those 4 methods use the same algorithm (Dijkstra).
the findings are located at the Wiki title.

#For more information about the project you welcome to watch Wiki title 😎 .