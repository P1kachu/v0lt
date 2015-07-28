class Stack:
    def __init__(self, verbose=False):
        self.container = []
        self.verbose = verbose

    def is_empty(self):
        return self.size() == 0

    def push(self, item):
        if self.verbose:
            print("<-- {0}".format(item))
        self.container.append(item)

    def pop(self):
        item = self.container.pop(-1)
        if self.verbose:
            print("--> {0}".format(item))
        return item  # pop from the container

    def size(self):
        return len(self.container)
