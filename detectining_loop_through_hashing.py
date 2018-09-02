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

	def detect(self):
				s=set()
				temp=self.head
				while(temp):
					if temp in s:
						return True
					s.add(temp)
					temp=temp.next	
				return False	

if __name__=="__main__":
	llist=LinkedList()
	llist.push(1)
	llist.push(2)
	llist.push(3)
	llist.push(4)

	llist.head.next.next.next.next=llist.head
	if(llist.detect()):
		print("Loop found")
	else:
		print("Loop Not Found")	
