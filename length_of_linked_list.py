class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
class LinkedList:
	def __init__(self):
		self.head=None
	def push(self,new_data)	:
		new_node=Node(new_data)
		new_node.next=self.head
		self.head=new_node
	
	def count(self,node):
		if not node:
			return 0
		else:
			return 1+self.count(node.next)		

	def count_begins(self):
		return self.count(self.head)		

if __name__=='__main__':
	llist=LinkedList()
	llist.push(4)
	llist.push(5)
	llist.push(6)
	llist.push(7)
	print(llist.count_begins())
			