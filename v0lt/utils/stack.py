class Stack:
    def __init__(self, verbose=False):
        self.little_stack = []
        self.verbose = verbose

    def is_empty(self):
        return self.size() == 0

    def push(self, item):
        if self.verbose:
            print("<-- {0}".format(item))
        self.little_stack.append(item)

    def pop(self):
        item = self.little_stack.pop(-1)
        if self.verbose:
            print("--> {0}".format(item))
        return item

    def size(self):
        return len(self.little_stack)
