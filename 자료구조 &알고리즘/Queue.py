class Queue():
    queue = []
    
    def enQueue(this, data):
        this.queue.append(data)
    
    def deQueue(this):
        return this.queue.pop()
    pass

queue = Queue()
queue.enQueue("첫 번째 데이터")
queue.enQueue("두 번째 데이터")
queue.enQueue("세 번째 데이터")

print(queue.deQueue())
print(queue.deQueue())
print(queue.deQueue())