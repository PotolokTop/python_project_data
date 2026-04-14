# stack (first in - last out)
class Stack:
    def __init__(self):
        self.__stack = [] # 
    
    def push(self, item):
        self.__stack.append(item)

    def pop(self):
        self.__stack.pop(-1)
    
    def size(self):
        return len(self.__stack)