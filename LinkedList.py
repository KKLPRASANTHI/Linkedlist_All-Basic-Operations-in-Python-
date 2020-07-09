class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def lenOfLL(self):
        temp=self.head
        c=0
        while(temp):
            c+=1
            temp=temp.next
        return c
    def insertAtStart(self,dt):
        print('Enter the node',end=' ')
        x=int(input())
        nnode=Node(x)
        if ll.head==None:
            ll.head=nnode
        else:
            '''
            temp=self.head
            self.head=nnode
            nnode.next=temp
            '''
            nnode.next=self.head
            self.head=nnode
        if dt!=10:
            print("Insertion at start successful")
    def insertAtEnd(self,val):
        print('Enter the node',end=' ')
        x=int(input())
        nnode=Node(x)
        if ll.head==None:
            ll.head=nnode
        else:
            temp=ll.head
            while temp.next!=None:
                temp=temp.next
            temp.next=nnode
        if val!=9:
            print("Insertion at end successful")
    def insertAtPos(self):
        print("Enter the position",end=" ")
        pos=int(input())
        lenh=ll.lenOfLL()
        if pos>lenh+1:
            print("No such position available")
            return
        elif pos==lenh+1:
            ll.insertAtEnd(9)
        elif pos==1:
            ll.insertAtStart(10)
        else:
            print('Enter the node',end=' ')
            x=int(input())
            nnode=Node(x)
            cnt=1
            temp=self.head
            while cnt<pos-1:
                temp=temp.next
                cnt+=1
            '''
            temp1=temp.next
            temp.next=nnode
            nnode.next=temp1
            '''
            nnode.next=temp.next
            temp.next=nnode
        print("Insertion at",pos,"successful")
    def deleteAtStart(self,dat):
        if self.head==None:
            print("List is empty")
            return
        else:
            temp=self.head
            self.head=temp.next
            temp=None#To delete Node from memory instead of just unlinking it from linked list
        if dat!=9:
            print("Deletion at start successful")
    def deleteAtEnd(self,tad):
        temp=self.head
        if temp==None:
            print("List is empty")
            return
        else:
            #lend=ll.lenOfLL()
            if temp.next==None:#if lend==1 or temp.next both mean same. Both indicate that list contains only one Node
                self.head=None
            else:
                while temp.next.next!=None:
                    temp=temp.next#We will reach the node just before the node to be deleted
                tempend=temp.next#Storing Nth node address in tempend,and then will set tempend to None. So that that node is deleted from memory
                temp.next=None
                #print("tempendBefore",tempend)#This prints some address, But the next print statement next to the below ine prints None, Because in the below line we deleted it, Instead of just unlinking it
                tempend=None#To delete that node instead of just delinking it
                #print("tempendAfter",tempend)
        if tad!=9:
            print("Deletion at end successful")
    def deleteAtPos(self):
        if self.head==None:
            print("List is empty")
        else:
            print("Enter the position",end=' ')
            dpos=int(input())
            if dpos<1:
                print("No such position available")
            elif dpos==1:
                ll.deleteAtStart(9)
            else:
                temp=self.head
                flag=False
                if temp.next is None and dpos!=1:#Here actually there is no need to verify dpos!=1 or not Becuase if it is 1 it will not come here, because the control has already entered the dpos==1 if block
                    flag=True
                else:
                    c=1
                    while(c<dpos-1):
                        c+=1
                        temp=temp.next
                        if temp is None or temp.next is None:
                            flag=True
                            break
                if flag:
                    print("No such position available")
                    return
                else:
                    tempd=temp.next#print("Before tempd",tempd)
                    temp.next=tempd.next#print("Before Deletion",tempd)
                    tempd=None#print("After Deletion",tempd)
                    #temp.next=temp.next.next
            print("Deletion at",dpos,"successful")
    def deleteKey(self):
        print("Enter the key value which you want to delete",end=" ")
        key=int(input())
        temp=self.head
        c=0
        #dellen=ll.lenOfLL()
        if temp==None:
            print("List is empty")
            return
        elif temp.next==None:#elif dellen==1 This temp.next ==None also means to say that the list is contatining only one node. So instead of calling ll.lenOfLL() to know wheter list length of list is 1 or not. we can just check if temp.next ==None. Which means he next part of 1st node is None, that means it is the only Node in the list
            if temp.data==key:
                self.head=None
            else:
                print("Key not found!!")
                return
        elif temp.data==key:
            #self.head=temp.next
            #temp=None
            ll.deleteAtStart(9)
        else:
            prev=None
            curr=self.head
            c=0
            #nxt=curr.next
            while(curr!=None):
                #nxt=curr.next
                if curr.data==key:
                    #print("HERE")
                    prev.next=curr.next
                    #print("Before curr",curr)
                    curr=None
                    #print("Before curr",curr)
                    c+=1
                    break
                else:
                    prev=curr
                    curr=curr.next
            if c==0:
                print("Key not found")
                return
            print(key,"deleted")
    def reverseLL(self):
            prev=None
            curr=self.head
            while(curr!=None):
                nxt=curr.next
                curr.next=prev
                prev=curr
                curr=nxt
            self.head=prev
    
    def recurReverse(self,curr):
        if curr.next==None:
            ll.head=curr
            return
        else:
            ll.recurReverse(curr.next)
            #temp=curr.next
            #temp.next=curr
            curr.next.next=curr
            curr.next=None
    def printReverse(self):
        temp=self.head
        rp=[]
        while temp:
            rp.insert(0,temp.data)
            temp=temp.next
        print(*rp,sep="-->")
    
    def recurReversePrint(self,temp):
        if temp==None:
            return
        else:
            ll.recurReversePrint(temp.next)
            if temp==ll.head:
                print(temp.data)
                return
            print(temp.data,end="-->")
                    #temp=temp.next
                    #ll.recurPrint(temp)The below line directly calls recurPrint function with temp.next instead of updating temp to temp.next and then calling recurPrint function with temp, what i did id i directly called recurPrint with updated value of temp just to reduce 1 line of code :-)                   
    def recurPrint(self,temp):
            #if temp.next==None:This condition is written seperately to not print a arrow mark to last node
                #print(temp.data)
            if temp.next==None:
                print(temp.data)
                return
            else:
                print(temp.data,end="-->")
                #temp=temp.next
                #ll.recurPrint(temp)The below line directly calls recurPrint function with temp.next instead of updating temp to temp.next and then calling recurPrint function with temp, what i did id i directly called recurPrint with updated value of temp just to reduce 1 line of code :-)
                ll.recurPrint(temp.next)
    def Display(self):
        temp=self.head
        while temp.next!=None:
            print(temp.data,end="-->")
            temp=temp.next
        print(temp.data)
    '''
    def printList(self):
        if self.head==None:
            print("List is empty")
            return
        temp=self.head
        while temp:
            if temp.next!=None:
                print(temp.data,"->",end=" ")
            else:
                print(temp.data)
            temp=temp.next
    '''
ll=LinkedList()
print("===============LINKED LIST MENU===============")
print("1.Inserton at start")
print("2.Insertion at end")
print("3.Insertion at postion")
print("4.Deletion at start")
print("5.Deletion at end")
print("6.Delete at position")
print("7.Delete a key")
print("8.Length of linked list")
print("9.Reverse the Linked List without using Recursion")
print("10.Reverse the linked list using recursion")
print("11.Print in Reverse(Without using recursion)")
print("12.Reverse print using recursion(Note: The actual linked List remains same, its only printed in reverse order)")
print("13. Print the Linked List Using recursion")
print("14.Display(Prints the Linked List using Iteration)")
print("0.Exit")
while True:
    print("Enter your choice",end=" ")
    ch=int(input())
    if ch==0:
        break
    elif ch==1:
        ll.insertAtStart(1)
    elif ch==2:
        ll.insertAtEnd(1)
    elif ch==3:
        ll.insertAtPos()
    elif ch==4:
        ll.deleteAtStart(1)
    elif ch==5:
        ll.deleteAtEnd(1)
    elif ch==6:
        ll.deleteAtPos()
    elif ch==7:
        ll.deleteKey()
    elif ch==8:
        leng=ll.lenOfLL()
        print("Length of the list is",leng)
    elif ch==9:
        if ll.head==None:
            print("List is Empty")
        else:
            ll.reverseLL()
    elif ch==10:
        lrec=ll.lenOfLL()
        if lrec==0:
            print("List is Empty")
        else:
            ll.recurReverse(ll.head)
    elif ch==11:
        if ll.head==None:
            print("Nothing to print :-)")
        else:
            ll.printReverse()
    elif ch==12:
        if ll.head==None:
            print("Nothing to print :-)")
        else:
            ll.recurReversePrint(ll.head)
    elif ch==13:
        if ll.head==None:
            print("Nothing to print :-)")
        else:
            ll.recurPrint(ll.head)       
    elif ch==14:
        if ll.head==None:
            print("Nothing to print :-)")
        else:
              ll.Display()
    else:
        print("Invalid choice Try again!!!")
        
