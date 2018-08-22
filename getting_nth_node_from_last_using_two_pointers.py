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


	def printlist(self):
		temp=self.head
		while temp!=None:
			print(temp.data)
			temp=temp.next		

	def getting_node(self,n):
		c=0
		ptr_first=self.head
		ptr_second=self.head

		while c<n:
			if ptr_second is None:
				print("n is greater than length of linked_list")
				return
			ptr_second=ptr_second.next
			c=c+1	
		while (ptr_second is not None):
			ptr_first=ptr_first.next
			ptr_second=ptr_second.next

		print("your node is ", (ptr_first.data))		

if __name__=="__main__":
	llist=LinkedList()
	llist.push(3)
	llist.push(32)
	llist.push(64)
	llist.push(128)
	llist.push(500)
	llist.printlist()
	llist.getting_node(2)


