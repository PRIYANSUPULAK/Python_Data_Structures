
class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

class LinkedList:
	def __init__(self):
		self.head=None

	def push(self,x):
		q=Node(x)
		q.next=self.head
		self.head=q

	def append(self,x):
		q=Node(x)
		if self.head==None:
			self.head=q
			return	
			
		temp=self.head
		while temp.next!=None:
			temp=temp.next
		temp.next=q
	
	def printlist(self):
		temp=self.head
		while temp!=None:
			print(temp.data)
			temp=temp.next		

	def  insertAfter(self,x,data):
		temp=self.head
		q=Node(data)
		while(temp.data!=x):
			temp=temp.next
		q.next=temp.next	
		temp.next=q	





llist=LinkedList()
llist.append(6)
llist.push(7)
llist.append(4)
llist.push(1)
llist.insertAfter(7,8)
llist.printlist()