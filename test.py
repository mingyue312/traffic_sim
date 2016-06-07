def append(link_list,target):
    current = link_list
    if current:
        while current.next != None:
            current = current.next
        current.next = target
    else:
        link_list = target


class Intersection:
    def __init__(self, name):
        self.name = name
        self.next = None
        self.prev = None

a = None

b = Intersection("Marco")

append(a,b)

print()