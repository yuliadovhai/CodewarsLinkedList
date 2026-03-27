from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
    
def get_nth(node, index):
    if node is None or index < 0 :
        raise Exception
    count = 0
    while node is not None:
        if count == index:
            return node
        node = node.next
        count += 1
    raise Exception
