class RingBuffer:
    def __init__(self, size):
        self.capacity = size
        self.data = [None for n in range(size)]
        self.start = 0
        self.next = 0
        self.length = 0
    def append(self, x):
        if self.next == self.start and self.length > 0 :
            self.start = (self.start+1)%self.capacity
            self.length -= 1
        self.data[self.next] = x
        self.next = (self.next+1)%self.capacity
        self.length += 1
    def remove(self):
        if self.next == self.start and self.length == 0 :
            return
        self.start = (self.start+1)%self.capacity
        self.length -= 1
    def get(self):
        result = [self.data[self.start]]
        x = self.start+1
        while x != self.next :
            result.append(self.data[x])
            x = (x+1)%self.capacity
        return result

N = long(raw_input())
rb = RingBuffer(N)
input = raw_input().split(" ")
while input[0] != "Q" :
    if input[0] == "A" :
        input[1] = long(input[1])
        for i in range(input[1]) :
            rb.append(raw_input())
    elif input[0] == "R" :
        input[1] = long(input[1])
        for i in range(input[1]) :
            rb.remove()
    elif input[0] == "L" :
        get = rb.get()
        for x in get :
            print(x)
    input = raw_input().split(" ")
