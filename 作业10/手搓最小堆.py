class MinHeap:
    def __init__(self):
        self.heap=[]
    
    def push(self,val):
        self.heap.append(val)
        self.up(len(self.heap)-1)

    def pop(self):
        if len(self.heap)==1:
            return self.heap.pop()
        Min=self.heap[0]
        self.heap[0]=self.heap.pop()
        self.down(0)
        return Min

    def up(self,index):
        while index>0:
            parent_index=(index-1)//2
            if self.heap[parent_index]>self.heap[index]:
                self.heap[parent_index],self.heap[index]=self.heap[index],self.heap[parent_index]
                index=parent_index
            else:
                break

    def down(self,index):
        while True:
            Min_index=index
            left_child=2*index+1
            right_child=2*index+2
            if left_child<len(self.heap) and self.heap[left_child]<self.heap[Min_index]:
                Min_index=left_child
            if right_child<len(self.heap) and self.heap[right_child]<self.heap[Min_index]:
                Min_index=right_child
            if Min_index==index:
                break
            self.heap[index],self.heap[Min_index] = self.heap[Min_index], self.heap[index]
            index = Min_index
            

n=int(input().strip())
heap=MinHeap()
for  _ in range(n):
    operation=list(map(int,input().strip().split()))
    if operation[0]==1:
        heap.push(operation[1])
    if operation[0]==2:
        print(heap.pop())



