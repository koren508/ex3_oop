class node_data:
    def __init__(self, id):
        self.id = id
        self.tag = 0
        self.info = ""
        self.pos = (0, 0, 0)
        self.weight = 0

    """
    init new node.
    """

    def __repr__(self):
        return repr((self.id, self.pos))

    """
    print the node.
    @return: print node
    """

    def get_id(self):
        return self.id

    """
    Returns the id of this node.
    @return: id of this node.
    """

    def get_tag(self):
        return self.tag

    """
    Returns the tag of this node.
    @return: tag of this node.
    """

    def get_info(self):
        return self.info

    """
    Returns the info of this node.
    @return: info of this node.
    """

    def get_pos(self):
        return self.pos

    """
    Returns the pos of this node.
    @return: pos of this node.
    """

    def get_weight(self):
        return self.weight

    """
    Returns the weight of this node.
    @return: weight of this node.
    """

    def set_id(self, newID):
        self.id = newID

        """
        set a new id with the given ID.
        """

    def set_tag(self, t):
        self.tag = t

        """
        set a new tag with the given t.
        """

    def set_info(self, newInfo):
        self.info = newInfo

        """
        set a new info with the given newInfo.
        """

    def set_pos(self, p):
        self.pos = p

        """
        set a new pos with the given p.
        """

    def set_weight(self, w):
        self.weight = w

        """
        set a new weight with the given w.
        """


class DiGraph:
    def __init__(self):
        self.graph = {}  # {id , node}
        self.connectionsSrc = {}  # {key , {key , weight} }
        self.connectionsDest = {}  # {key , {key , weight} }
        self.numNodes = 0
        self.numEdges = 0
        self.changes = 0

    """
    init the graph.
    """

    def __repr__(self):
        ll = []
        strr = f"Graph: |V|={self.numNodes} , |E|= {self.numEdges}"
        last = []
        for i in self.graph:
            temp = f"{i}: {i}: |edges out| {len(self.all_out_edges_of_node(i))} |edges in| {len(self.all_in_edges_of_node(i))}"
            ll.append(temp)
        second_row = " , ".join(ll)
        last.append(strr)
        last.append(second_row)
        final_string = "\n{".join(last)
        final_string = final_string + "}"
        return final_string

    """
    print the graph.
    @return print the graph.
    """

    def v_size(self):
        return self.numNodes
    """
    Returns the number of vertices in this graph
    @return: The number of vertices in this graph
    """

    def e_size(self):
        return self.numEdges
    """
    Returns the number of edges in this graph
    @return: The number of edges in this graph
    """

    def get_all_v(self):
        return self.graph

    """return a dictionary of all the nodes in the Graph, each node is represented using a pair
     (node_id, node_data)
    """

    def all_in_edges_of_node(self, id1):
        return self.connectionsDest[id1]

    """return a dictionary of all the nodes connected into node_id ,
    each node is represented using a pair (other_node_id, weight)
     """

    def all_out_edges_of_node(self, id1):
        return self.connectionsSrc[id1]

    """return a dictionary of all the nodes connected from node_id , each node is represented using a pair
    (other_node_id, weight)
    """

    def get_mc(self):
        return self.changes

    """
    Returns the number of changes no the graph.
    such as: addNode , removeNode , addEdge , removeEdge.
    @return: The current version of this graph.
    """

    def add_edge(self, id1, id2, weight):
        if id1 == id2:
            return False
        if id1 in self.graph and id2 in self.graph:
            if id2 in self.connectionsSrc.get(id1):
                return False
            else:
                self.connectionsSrc[id1][id2] = weight
                self.connectionsDest[id2][id1] = weight
                self.changes += 1
                self.numEdges += 1
                return True
        else:
            return False

    """
    Adds an edge to the graph.
    @param id1: The start node of the edge
    @param id2: The end node of the edge
    @param weight: The weight of the edge
    @return: True if the edge was added successfully, False o.w.

    Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
    """

    def get_node(self, id: int) -> node_data:
        if id in self.graph:
            return self.graph.get(id)

    """
    Return the node with the given id.
    @param node_id: The node ID
    @return: the node with the given id.
    """

    def add_node(self, node_id):
        if node_id in self.graph:
            return False
        else:
            temp = node_data(node_id)
            self.graph[node_id] = temp
            self.connectionsDest[node_id] = {}
            self.connectionsSrc[node_id] = {}
            self.numNodes += 1
            self.changes += 1
            return True

    """
    Adds a node to the graph.
    @param node_id: The node ID
    @param pos: The position of the node
    @return: True if the node was added successfully, False o.w.

    Note: if the node id already exists the node will not be added
    """

    def remove_node(self, node_id):
        if node_id not in self.graph:
            return False

        self.graph.pop(node_id)
        self.numNodes -= 1
        self.changes += 1
        if len(self.connectionsSrc[node_id]) != 0:
            for x in self.connectionsSrc[node_id]:
                self.connectionsDest.get(x, {}).pop(node_id)
                # self.changes += 1
                self.numEdges -= 1
        self.connectionsSrc.pop(node_id)

        if len(self.connectionsDest[node_id]) != 0:
            for x in self.connectionsDest[node_id]:
                self.connectionsSrc.get(x, {}).pop(node_id)
                # self.changes += 1
                self.numEdges -= 1
        self.connectionsDest.pop(node_id)

    """
    Removes a node from the graph.
    @param node_id: The node ID
    @return: True if the node was removed successfully, False o.w.

    Note: if the node id does not exists the function will do nothing
    """

    def remove_edge(self, node_id1, node_id2):
        if node_id1 in self.graph and node_id2 in self.graph:
            if node_id2 in self.connectionsSrc[node_id1]:
                self.connectionsSrc.get(node_id1, {}).pop(node_id2)
                self.connectionsDest.get(node_id2, {}).pop(node_id1)
                self.numEdges -= 1
                self.changes += 1
                return True
            else:
                return False
        else:
            return False

    """
    Removes an edge from the graph.
    @param node_id1: The start node of the edge
    @param node_id2: The end node of the edge
    @return: True if the edge was removed successfully, False o.w.

    Note: If such an edge does not exists the function will do nothing
    """
