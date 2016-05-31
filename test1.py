

class car:
    def __init__(self, value):
        self.next = None
        self.prev = None
        self.value = value


car1 = car(1)
car2 = car(2)
car3 = car(3)
car1.next = car2
car2.prev = car1
car2.next = car3
car3.prev = car2


car4 = car(4)

car1.next = car2.next
car3.prev = car1

a = car3.next
if a != None:
    print 1