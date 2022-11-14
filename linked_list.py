# linked list implementation

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class linked_list:
    def __init__(self):
        self.head = None

    # insert at the begining
    def insert_at_begingig(self, data):
        node = Node(data=data, next=self.head)
        self.head = node

    # inset at end
    def insert_at_end(self, data):
        if self.head is None:
            self.insert_at_begingig(data)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data=data)

    # insert multi values
    def insert_values(self, values):
        for elem in values:
            self.insert_at_end(elem)

    #  get length methods
    def get_len(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count

    # remove by index
    def remove_at(self, index):
        if index >= self.get_len() or index < 0:

            raise IndexError("my_error  : index error ")
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr.next:
            if count == index - 1:
                itr.next = itr.next.next
                break
            count += 1
            itr = itr.next
    # inser at index
    def insert_at(self,index,data):
      if index < 0 or index > self.get_len():
        raise Exception("insert index error in 62 line ")
      if index ==0:
        self.head = Node(data= data , next= self.head)
        return
      count = 0
      itr  = self.head.next
      while itr.next:
        if count == index -1  :
          itr.next = Node(data= data , next= itr.next)
          break
        count +=1
        itr =itr.next


    # print total linked list

    def print(self):
        if self.head == None:
            print("linked list is error ")
            return
        itr = self.head
        while itr:
            print(itr.data, end=",")
            itr = itr.next


if __name__ == "__main__":
    ls = linked_list()
    #  insert begining
    # ls.insert_at_begingig("2")
    # ls.insert_at_begingig("1")
    #  insert end
    # ls.insert_at_end("3")
    # ls.insert_at_end("4")
    #  insert ending
    ls.insert_values(["5", "6","7",'8',"9"])
    ls.insert_at(3, "insert")
    ls.print()
    #  print("list count is :",ls.get_len())

    # ls.remove_at(3)

    #  print("list count is :",ls.get_len())
