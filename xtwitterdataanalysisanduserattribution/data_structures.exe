
from person import *

#linked list

class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.next = None     

class LinkedList:
    def __init__(self):
        self.head = None
    def to_list(self):
        items = []
        current = self.head
        while current:
            items.append(current.data)
            current = current.next
        return items
    
    def insert(self, key, data):
       #print(f"Data: {data}")
        if self.head is None:
            self.head = Node(key, data)
        else:
            current = self.head
            while current.next:
                if current.key == key:
                    current.data = data  # Anahtar zaten varsa, veriyi güncelle
                    return
                current = current.next
            #print(f"Key:{key}, data: {data}")
            current.next = Node(key, data)  # Yeni düğüm ekle   

    def find(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current.data
            current = current.next   
        return None  # Anahtar bulunamazsa None dön
    
    
    def set(self,key,val):
        current = self.head
        while current:
            if current.key == key:
               current.data=val
            current = current.next      
        return None

    def max(self):
        current = self.head
        temp = 0
        key = None
        while current:
            if current.data > temp:
               temp=current.data
               key = current.key
            current = current.next     
        return key             
    
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
    
    def create(self, key):
        if self.head is None:
            self.head = Node(key, None)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(key, None)     
#list yapısı için 
# gerekirse key eklerim key arttırıp veririm  indexs key olur ona gore ararım
		
class kok:
    def __init__(self, data):
        self.data = data
        self.next = None

class myList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        if self.head is None:
            self.head = kok( data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = kok( data)  # Yeni düğüm ekle

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def find(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current.data
            current = current.next     
        return None
    
    def extend(self, other):
        current = self.head
        if current is None:
            self.head = other.head
        else:
            while current.next:
                current = current.next
            current.next = other.head

    def delete(self, data):
        current = self.head
        prev = None
        while current:
            if current.data == data:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return
            prev = current
            current = current.next        

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front is None

    def enqueue(self, item):
        temp = kok(item)

        if self.rear is None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    def dequeue(self):
        if self.isEmpty():
            return None
        temp = self.front
        self.front = temp.next

        if self.front is None:
            self.rear = None
        return temp.data
#hashmap           
            
class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [LinkedList() for i in range(self.MAX)]
        #print(f"self array: {self.arr}")
    
    def get_hash(self, key):
        if isinstance(key, str):
            hash = 0
            for char in key:
                hash += ord(char)
            return hash % self.MAX
        else:
              return self.get_hash(str(key))
    
    def __getitem__(self, key):
        arr_index = self.get_hash(key)
        return self.arr[arr_index].find(key)
    
    def get_items(self):
        items = []
        for linked_list in self.arr:
            current_node = linked_list.head
            while current_node:
                items.append((current_node.key, current_node.data))
                current_node = current_node.next
        return items
    
    def find(self, key):
        arr_index = self.get_hash(key)
        return self.arr[arr_index].find(key)


    def __setitem__(self, key, value):
        # Eğer value bir person_info nesnesi ise, key olarak  username kullan
        if isinstance(value, person_info):
            key = value.person.username
        arr_index = self.get_hash(key)
        #print(f"arr_index: {arr_index}")
        #print(f"Inserting key: {key}")
        #print(f"Value: {value}")
        self.arr[arr_index].insert(key, value)
    
    def __delitem__(self, key):
        arr_index = self.get_hash(key)
        self.arr[arr_index].delete(key)

    def create(self,key,):
        arr_index = self.get_hash(key)
        self.arr[arr_index].create(key)

    def find_common_words(self, limit):
        word_counts = {}
        for linked_list in self.arr:
            current = linked_list.head
            while current:
                if current.key in word_counts:
                    word_counts[current.key] += 1
                else:
                    word_counts[current.key] = 1
                current = current.next

        most_common = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:limit]
        return most_common    
      
class Nodet:
	def __init__(self, val):
		self.left = None
		self.right = None
		self.data = val

class Binary_Tree:
	def __init__(self):
		self.root = None

	def getRoot(self):
		return self.root.data

	def add(self, val):
		if self.root == None:
			self.root = Nodet(val)
		else:
			self._add(val, self.root)

	def _add(self, val, node):
		if val < node.data:
			if node.left != None:
				self._add(val, node.left)
			else:
				node.left = Nodet(val)
		else:
			if node.right != None:
				self._add(val, node.right)
			else:
				node.right = Nodet(val)

	def printTree(self, trav = "in"):
		if self.root != None:
			if trav == "in":
				self.printTree_in(self.root)
			elif trav == "pre":
				self.printTree_pre(self.root)
			elif trav == "post":
				self.printTree_post(self.root)
		
	def printTree_in(self, node):
		if node == None:
			return
		self.printTree_in(node.left)
		print(node.data)
		self.printTree_in(node.right)

	def printTree_pre(self, node):
		if node == None:
			return
		print(node.data)
		self.printTree_pre(node.left)
		self.printTree_pre(node.right)

	def printTree_post(self, node):
		if node == None:
			return
		self.printTree_post(node.left)
		self.printTree_post(node.right)
		print(node.data)

class Set:
    def __init__(self):
        self.set = myList()

    def add(self, data):
        if not self.contains(data):
            self.set.insert(data)

    def contains(self, data):
        current = self.set.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

"""

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        else:
            return None

    def size(self):
        return len(self.items)
"""