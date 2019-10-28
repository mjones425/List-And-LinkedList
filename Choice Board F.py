''' Marquetta Jones
October 24, 2019
Linked List Choice Board: F '''

#class definition for Node
class Node:
    def __init__(self, info):
        self.info = info
        self.link = None

#class definition for LinkedList
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_start(self, info):
        temp = Node(info)
        temp.link = self.head
        self.head= temp
        
    def traverse_list(self):
        if self.head is None:
            print("List has no element")
            return
        else:
            current = self.head
            while current is not None:
                print(current.info , " ")
                current = current.link

    def count(self):
        count = 0
        if self.head is None:
            print("List has no element")
            return
        else:
            current = self.head
            while current is not None:
                count += 1
                current = current.link
            print("Total:", count)

    def minimum(self):
        if self.head is None:
            print("List has no element")
            return
        else:
            current = self.head
            minimum = current.info 
            while current is not None:
                if minimum > current.info:
                    minimum = current.info
                current = current.link
            return minimum

def maximum(listt):
    maximum = listt[0]
    for x in range(len(listt)):
        if listt[x] > maximum:
            maximum = listt[x]
    return maximum

def main():
    oddNums = LinkedList()
    evenNums = []
    infile = open('numbers.txt','r')
    num = infile.readline()
    while num != "":
        num = int(num.rstrip("\n"))
        if num%2 == 0:
            evenNums.append(num)
        else:
            oddNums.insert_at_start(num)
        num = infile.readline()
    infile.close()

    print("Odd Numbers:")
    oddNums.traverse_list()
    print("Minimum Odd Number:", oddNums.minimum())
    
    print("Even Numbers:")
    print(evenNums)
    print("Maximum Even Number:", maximum(evenNums))
    
main()
        
