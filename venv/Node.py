
class Node:
    """
    This class present Node (or vertex)
    """

    def __init__(self , ID:int = -1 ,loc:tuple = None, Info:str = "white" , Tag:bool = False , EdgesOut:dict = None ,EdgesIn:dict = None , Weight:float = 0 , Prev = None):
        """
        constractor
        :param ID: The value of the node
        :param loc: the location of the node
        :param Info: the color of the node (for dijkstra algorithm)
        :param Tag: visited/not visited
        :param EdgesOut: dictionary that holds all the edges it sends To his neighbors
        :param EdgesIn:  dictionary that holds all the edges it getting from his neighbors
        :param Weight: (for dijkstra algorithm)
        :param Prev: The previous node from which we came (for dijkstra algorithm)
        """
        self.id = ID
        self.info = Info
        self.tag = Tag
        self.location = loc
        self.weight = Weight
        self.prev = Prev

        if EdgesOut != None:
            self.edges_out = EdgesOut
        else:
            self.edges_out = {}  # {idNode :int , weight :float}
        if EdgesIn != None:
            self.edges_in = EdgesIn
        else:
            self.edges_in = {}  # {idNode :int , weight :float}


    def __repr__(self):
        return str(self.__dict__)


    def __eq__(self, other) -> bool:
        return self.location == other.location and  self.id == other.id

    def __lt__(self, other):
        p = (self.weight, self.id)
        h = (other.weight, other.id)
        if p < h:
            return True
        else:
            return False


    def repr_json(self):
        return self.__dict__
