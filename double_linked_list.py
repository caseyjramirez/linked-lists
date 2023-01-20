class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data;
        self.prev = prev;
        self.next = next;

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_beginning(self, data):
        node = Node(data, None, self.head);
        if self.head:
            self.head.prev = node;
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None);
        
        itr = self.head;

        while itr.next:
            itr = itr.next;

        itr.next = Node(data, itr, None);

    def insert_values(self, data_list):
        self.head = None;

        for data in data_list:
            print(data)
            self.insert_at_end(data)

    def print(self):
        if self.head is None:
            print("No Data!")
        else:
            itr = self.head;
            dllstr = '';

            while itr:
                if itr.next and itr.prev:
                    dllstr += " <-- " + str(itr.data) + " --> ";
                elif itr.next:
                    dllstr += str(itr.data) + " --> ";
                elif itr.prev:
                    dllstr += " <-- " + str(itr.data);
                else:
                    dllstr += str(itr.data);
                
                itr = itr.next;
            
            print(dllstr);



if __name__ == "__main__":
    dll = DoubleLinkedList()
    # dll.insert_at_beginning(3)
    # dll.insert_at_beginning(2)
    # dll.insert_at_beginning(1)
    # dll.insert_at_end(4)
    # dll.insert_at_end(5)
    dll.insert_values(['apple', 'orange', 'mango'])
    dll.print()