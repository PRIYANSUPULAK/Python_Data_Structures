# your code goes here
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

	def detect_loop(self):
		slow=self.head
		fast=self.head
		while(slow!=None and fast!=None and fast.next!=None):
			slow=slow.next
			fast=fast.next.next

			if slow==fast:
				print("Loop Found")
				return

		print("Loop Not Found")
		return

if __name__=="__main__":
	llist=LinkedList()
	llist.push(1)
	llist.push(2)
	llist.push(3)
	llist.push(4)

# making a loop
	llist.head.next.next.next.next=llist.head
	llist.detect_loop()
