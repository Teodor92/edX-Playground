class Queue(object):

    def __init__(self):
        self.values = []

    def insert(self, element):
        self.values.append(element)
        
    def remove(self):
        try:
            return self.values.pop()
        except:
            raise ValueError()
        