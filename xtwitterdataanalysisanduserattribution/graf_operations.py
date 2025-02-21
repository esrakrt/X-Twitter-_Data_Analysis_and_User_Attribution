from PyQt5.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from data_structures import Set,myList,Queue,HashTable




class GraphVisualizer(QWidget):
    def __init__(self, graph,followers,following):
        super().__init__()
        self.graph = graph 
        self.followers = followers
        self.following = following
        self.initUI(followers, following)

    def initUI(self,followers,following):
        self.setGeometry(100, 100, 1000, 1000)
        self.setWindowTitle('Graph Visualization')

        layout = QVBoxLayout()
        self.setLayout(layout)
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.fig)
        layout.addWidget(self.canvas)
       
        self.drawGraph(followers,following)

    def drawGraph(self, followers, following):
        self.ax.clear()

        G = nx.DiGraph()

        for key in self.graph.vertList:
            G.add_node(key)

        for key, value in self.graph.vertList.items():
            connected_nodes = value.connections.get_items()
            for node in connected_nodes:
                G.add_edge(key, node)

        positions = nx.spring_layout(G, seed=92 ,k=0.5)

        followers_edges = [(node, neighbor) for node, neighbor in G.edges() if node in followers]
        following_edges = [(node, neighbor) for node, neighbor in G.edges() if node in following]
        
        nx.draw(G, pos=positions, ax=self.ax, node_size=100, node_color='skyblue', font_weight='bold', with_labels=False, arrows=True, arrowsize=20, width=2, edge_color='gray')

        nx.draw_networkx_edges(G, pos=positions, edgelist=followers_edges, edge_color='blue',
                       ax=self.ax, width=2, arrows=True, arrowsize=40)
        nx.draw_networkx_edges(G, pos=positions, edgelist=following_edges, edge_color='red',
                       ax=self.ax, width=1.5, arrows=True, arrowsize=40)
        for node in self.followers:
         if node in positions:  # Check if node is in positions
            nx.draw_networkx_nodes(G, pos=positions, nodelist=[node], ax=self.ax, node_color='green', node_size=70)
         else:
            print(f"Node {node} has no position. Skipping this node.")

        for edge in G.edges():
            start_pos = positions[edge[0]]
            end_pos = positions[edge[1]]
            x = np.mean([start_pos[0], end_pos[0]])
            y = np.mean([start_pos[1], end_pos[1]])
            self.ax.text(x, y, f'{edge[0]} -> {edge[1]}', horizontalalignment='center', verticalalignment='center', fontsize=6)

        for node, position in positions.items():
            if node in self.followers or node in self.following:
                text = f'{node}'
                self.ax.text(position[0], position[1], text, ha='center', va='center', fontsize=6, color='black')
        
        x_center, y_center = np.mean([position[0] for position in positions.values()]), np.mean([position[1] for position in positions.values()])
        xlim, ylim = self.ax.get_xlim(), self.ax.get_ylim()
        self.ax.text(x_center, y_center, '', ha='center', va='center', fontsize=6, color='white')
        self.ax.set_xlim(xlim)
        self.ax.set_ylim(ylim)
        
        self.canvas.figure.tight_layout()
        plt.show()

class LinkedListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class Node:
    def __init__(self, key,value):
        self.key = key
        self.connections = LinkedList_graph()
        self.value = value


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key,value):
        if key not in self.vertList:
            self.numVertices += 1
            newVertex = Node(key,value)
            self.vertList[key] = newVertex
            value = value


    def getVertex(self, key):
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None

    def addEdge(self, k1, k2):
        if k1 not in self.vertList:
            self.addVertex(k1)
        if k2 not in self.vertList:
            self.addVertex(k2,None)
        self.vertList[k1].connections.insert(k2)
        self.vertList[k2].connections.insert(k1)

    def getVertices(self):
        return list(self.vertList.keys())

class LinkedList_graph:
    def __init__(self):
        self.head = None
        self.node_map = {}  # Anahtarları ve düğümleri saklamak için bir sözlük

    def insert(self, key):
        if key not in self.node_map:
            new_node = LinkedListNode(key)
            self.node_map[key] = new_node
            if self.head is None:
                self.head = new_node
            else:
                current = self.head
                while current.next:
                    current = current.next
                current.next = new_node

    def find(self, key):
        return self.node_map.get(key, None)
    
    def get_items(self):
        items = []
        current = self.head
        while current:
            items.append(current.key)
            current = current.next
        return items

    def delete(self, key):
        current = self.head
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                del self.node_map[key]  # Anahtarı da sil
                return
            prev = current
            current = current.next

    def get_items(self):
        items = []
        current = self.head
        while current:
            items.append(current.key)
            current = current.next
        return items



def bfs(graph, start, table):
    visited = Set()
    queue = Queue()
    same_followers = HashTable()

    queue.enqueue(start.person.username)

    while not queue.isEmpty():
        vertex = table.__getitem__(queue.dequeue())

        users_list = same_followers.__getitem__(vertex.person.followers_count)
        if users_list is None:
            same_followers.__setitem__(vertex.person.followers_count, [vertex.person.username])
        else:
            users_list.append(vertex.person.username)
            same_followers.__setitem__(vertex.person.followers_count, users_list)

        for neighbour in graph.getVertex(vertex).connections.get_items():
            if not visited.contains(neighbour):
                visited.add(neighbour)
                queue.enqueue(neighbour)
    return same_followers


"""
herkesin ilgi alanını modelle bulurum 
bolge ve dille ilgili hastag leri kelime saydırırım"""
""" 
def bfs(users):
    i=0
    #kendi set yapım ve {} yerine hash table la  
    visited = Set()
    same_followers = HashTable()

    for start_user in users:
        visited.add(start_user.person.username)
        queue = Queue()

        queue.enqueue(start_user)
        while not queue.isEmpty():
            current_user = queue.dequeue()
            for user in users:
                if  visited.contains(user.person.username)== None and user.person.followers_count == current_user.person.followers_count:
                    queue.enqueue(user)
                    visited.add(user.person.username)
                    if same_followers.find(current_user.person.followers_count) is None:
                        users_list =myList()
                        same_followers.__setitem__(current_user.person.followers_count, users_list)
                    users_list.insert(user.person.username) 
            i = i + 1
        print(f"i = {i}")                         
    return same_followers
"""
"""
    def has_edge(self, node1, node2):
         return node1.connections.find(node2.key) is not None or node2.connections.find(node1.key) is not None
 """ 
"""
class LinkedList_graph:
    def __init__(self):
        self.head = None

    def insert(self, key):
        if self.head is None:
            self.head = LinkedListNode(key)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = LinkedListNode(key)
    
    def find(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current
            current = current.next
        return None
    
    def delete(self, key):
        current = self.head
        prev = None
        while current:
            if current.key == key: 
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return
            prev = current
            current = current.next

    def get_items(self):
        items = []
        current = self.head
        while current:
            items.append(current.key)
            current = current.next
        return items
        
"""
  