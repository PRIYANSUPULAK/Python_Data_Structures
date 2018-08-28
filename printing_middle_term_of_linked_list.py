class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

class LinkedList:
	def __init__(self):
		self.head=None

	def push(self,data):
		new_node=Node(data)
		new_node.next=self.head
		self.head=new_node

	def middle(self):
		first_ptr=self.head
		second_ptr=self.head
		while(first_ptr.next!=None):
			first_ptr=first_ptr.next.next
			second_ptr=second_ptr.next

		print(second_ptr.data)				

if __name__=="__main__":
	llist=LinkedList()
	llist.push(1)
	llist.push(2)
	llist.push(9)
	llist.push(4)
	llist.push(5)
	llist.middle()
