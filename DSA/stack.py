

class Stack:
    def __init__(self, stack):
        self.stack = stack

    def push(self, value):
        self.stack.append(value)


    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()
    
    def peek(self):
        if len(self.stack) == 0:
            return None
        return self.stack[len(self.stack)-1]

    def size(self):
        return len(self.stack)


if __name__ == "__main__":
    myStack = ["robert", "shawn", "don"]
    print(Stack(myStack).peek())




