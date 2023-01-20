# individual element in a LL
class Node:
    def __init__(self, data=None, next=None):
        self.data = data;
        self.next = next;

# head points to the head of the LL
class LinkedList:
    def __init__(self):
        self.head = None;

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node;
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None);
            return;
        else:
            itr = self.head;
            while itr.next:
                itr = itr.next;
            
            itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None;

        for data in data_list:
            self.insert_at_end(data)
    
    def get_length(self):
        itr = self.head;
        count = 0;
        while itr:
            count += 1;
            itr = itr.next;
        
        return count;
    
    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index");
        
        if index == 0:
            self.head = self.head.next;
        
        counter =  0;
        itr = self.head
        while itr:
            if counter == index - 1:
                itr.next = itr.next.next;
                break;

            itr = itr.next;
            counter += 1;
    
    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index");

        if index == 0:            
            self.insert_at_beginning(data);
            return;
        
        counter = 0;
        itr = self.head;
        
        while itr:
            if counter == index - 1:
                itr.next = Node(data, itr.next);
                break;
            itr = itr.next;
            counter += 1;


    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head;

        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next);
                return;
            itr = itr.next;
        
        print("Invalid Data!");
        return;

    def remove_by_value(self, data):
        itr = self.head;
        counter = 0;

        while itr:
            if itr.data == data:
                self.remove_at(counter);
                return;
            else:
                itr = itr.next;
                counter += 1;
        
        print("Invalid Data!");
        return;





    def print(self):
        if self.head is None:
            print("Linked List is empty!")
            return
        else:
            itr = self.head;
            llstr = '';
            while itr:
                if itr.next:
                    llstr += str(itr.data) + "-->";
                else:
                    llstr += str(itr.data);
                    
                itr = itr.next;
            
            print(llstr);


if __name__ == "__main__":
    ll = LinkedList();

    # ll.insert_at_beginning(5);
    # ll.insert_at_beginning(89);
    # ll.insert_at_end(45)
    # ll.insert_at_beginning(9);

    ll.insert_values(['apple', 'orange', 'mango'])

    # ll.print();
    # print(ll.get_length())
    # ll.insert_at(3, "grapes");
    ll.insert_after_value("apple", "clementine");
    ll.remove_by_value("asfdasf")
    # print(ll.get_length())
    ll.print();

    # ll.insert_after_value("orange", "mango");

