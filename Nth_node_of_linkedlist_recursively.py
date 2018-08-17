
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

	def searching(self, node, n):
		if n==1:
			return node.data
		
		if(node.next is None):
			return ("position not available")
				
		return self.searching(node.next,n-1)
				
	def search(self,position):
		n=position
		return self.searching(self.head,n)		

if __name__=='__main__':
	llist=LinkedList()
	llist.push(3)
	llist.push(8)
	llist.push(7)
	llist.push(1)
	llist.push(12)

	print(llist.search(6))

