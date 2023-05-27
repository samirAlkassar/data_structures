class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        # create a new node with the given data
        new_node = Node(data)

        # if the linked list is empty, set the new node as the head
        if self.head is None:
            self.head = new_node
            return

        # traverse to the end of the linked list
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next

        # set the new node as the next node of the last node
        current_node.next = new_node

    def display(self):
        # traverse through the linked list and print each node's data
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")
    
    def delete(self, data):
        # if the linked list is empty, return
        if self.head is None:
            return

        # if the head node contains the data, set the next node as the new head
        if self.head.data == data:
            self.head = self.head.next
            return        # traverse through the linked list to find the node with the given data
        current_node = self.head
        while current_node.next is not None:
            # if the next node contains the data, set the current node's next to the next node's next
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next
