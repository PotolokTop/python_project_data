# дана строка со значениями "(" "[" "{" ")" "}" "]" 
# убедиться в следующем: 1) скобки должны быть закрыты;
# 2) скобки должны быть в определенном порядке
s = "[()][)][{" # строка символов

pairs = {
    "(": ")",
    "[": "]",
}

class Stack:
    def __init__(self):
        self.__stack = [] # массив
    
    def push(self, item): # добавить элемент
        self.__stack.append(item)

    def pop(self): # удалить элемент
        self.__stack.pop(-1) 

    def peek(self): # последний элемент
        return self.__stack[len(self.__stack)-1]
    
    def show(self): # вывод стека
        print(self.__stack)

stack = Stack()

stack.push(s[0])
for ch in s:
    stack.push(pairs.get(ch))

stack.show()
        
        # Stack.push(ch)
