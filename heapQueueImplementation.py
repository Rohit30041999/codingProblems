'''
Concept: Heaps ==> (I) Min heap and 
                   (II) Max heap
Note: 1) Heaps or HeapQueues can also be called as Priority Queues. 
      2) Min and Max heaps are just conditions to store elements or data into a Heap Queue or Priority Queue.
'''

# Priority Queue or Heap Queue class
class heapQueue(object):
    def __init__(self, arr: list, requirement: str) -> None:
        self.arr = arr
        self.store = [0]*len(arr)
        if requirement == 'min heap':
            self.heapify_MIN(self.store, arr)
        if requirement == 'max heap':
            self.heapify_MAX(self.store, arr)

    # Min heapify or (Min Heap condition)
    def heapify_MIN(self, heap: list, arr: list) -> None:
        index = 0
        for i in range(0, len(arr)):
            heap[index] = arr[i]
            j, ii = i, i
            while j >= 0:
                if heap[j] > heap[ii]:
                    heap[ii], heap[j] = heap[j], heap[ii]
                    ii = j
                if j % 2 == 0:
                    j = (j - 2)//2
                elif j % 2 != 0:
                    j = (j - 1)//2
            index += 1

        for i in range(len(heap)):
            arr[i] = heap[i]
    
    # Max heapify or (Max Heap condition)
    def heapify_MAX(self, heap: list, arr: list) -> None:
        index = 0
        for i in range(0, len(arr)):
            heap[index] = arr[i]
            j, ii = i, i
            while j >= 0:
                if heap[j] < heap[ii]:
                    heap[ii], heap[j], = heap[j], heap[ii]
                    ii = j
                if j % 2 == 0:
                    j = (j - 2)//2
                elif j % 2 != 0:
                    j = (j - 1)//2
            index += 1

        for i in range(len(heap)):
            arr[i] = heap[i]

    # Just returns the Min Value
    def getMinValue(self, data: list) -> int:
        return data[0]

    # Just returns the Max Value
    def getMaxValue(self, data: list) -> int:
        return data[0]

    # Returns the Minimum Value by removing it from the heap
    def getMinByDeletingIt(self, data: list) -> int:
        requiredMinValue = data[0]
        j = 0

        while j <= len(data)-1:
            leftChild, rightChild = pow(2, 63)-1, pow(2, 63)-1
            leftChildIndex, rightChildIndex = ((2 * j) + 1), ((2 * j) + 2)
            if leftChildIndex <= len(data)-1:
                leftChild = data[leftChildIndex]
            if rightChildIndex <= len(data)-1:
                rightChild = data[rightChildIndex]
            data[j] = min(leftChild, rightChild) if (leftChild != pow(2, 63)-1) or (rightChild != pow(2, 63)-1) else 0
            if (data[j] == leftChild and leftChild != pow(2, 63)-1) or data[j] == 0:
                while data[j] == 0 and j < len(data)-1:
                    data[j], data[j+1] = data[j+1], data[j]
                    ii, i = j, j
                    while i >= 0:
                        if data[i] > data[ii]:
                            data[ii], data[i] = data[i], data[ii]
                            ii = i
                        if i % 2 == 0:
                            i = (i - 2)//2
                        elif i % 2 != 0:
                            i = (i - 1)//2
                    j = j + 1
                j = leftChildIndex
            elif (data[j] == rightChild and rightChild != pow(2, 63)-1) or data[j] == 0:
                while data[0] == 0 and j < len(data)-1:
                    data[j], data[j+1] = data[j+1], data[j]
                    ii, i = j, j
                    while i >= 0:
                        if data[i] > data[ii]:
                            data[ii], data[i] = data[i], data[ii]
                            ii = i
                        if i % 2 == 0:
                            i = (i - 2)//2
                        elif i % 2 != 0:
                            i = (i - 1)//2
                    j = j + 1
                j = rightChildIndex
        
        data.pop()

        return requiredMinValue

    # Returns the Maximum Value by removing it from the heap
    def getMaxByDeletingIt(self, data: list) -> int:
        requiredMaxValue = data[0]
        j = 0

        while j <= len(data)-1:
            leftChild, rightChild = -pow(2, 63), -pow(2, 63)
            leftChildIndex, rightChildIndex = ((2 * j) + 1), ((2 * j) + 2)
            if leftChildIndex <= len(data)-1:
                leftChild = data[leftChildIndex]
            if rightChildIndex <= len(data)-1:
                rightChild = data[rightChildIndex]
            data[j] = max(leftChild, rightChild) if (leftChild != -pow(2, 63)) or (rightChild != -pow(2, 63)) else 0
            if (data[j] == leftChild and leftChild != -pow(2, 63)) or data[j] == 0:
                while data[j] == 0 and j < len(data)-1:
                    data[j], data[j+1] = data[j+1], data[j]
                    ii, i = j, j
                    while i >= 0:
                        if data[i] < data[ii]:
                            data[ii], data[i] = data[i], data[ii]
                            ii = i
                        if i % 2 == 0:
                            i = (i - 2)//2
                        elif i % 2 != 0:
                            i = (i - 1)//2
                    j = j + 1
                j = leftChildIndex
            elif (data[j] == rightChild and rightChild != -pow(2, 63)) or data[j] == 0:
                while data[j] == 0 and j < len(data)-1:
                    data[j], data[j+1] = data[j+1], data[j]
                    ii, i = j, j
                    while i >= 0:
                        if data[i] < data[ii]:
                            data[ii], data[i] = data[i], data[ii]
                            ii = i
                        if i % 2 == 0:
                            i = (i - 2)//2
                        elif i % 2 != 0:
                            i = (i - 1)//2
                    j = j + 1
                j = rightChildIndex

        data.pop() 

        return requiredMaxValue

# main function
def main():
    data, requirement = list(map(int, input("Enter your data \n").strip().split())), input("min heap or max heap: \n").strip()
    heapq = heapQueue(data, requirement)
    if requirement == 'max heap':
        print("Max Heap data before picking put the max value :")
        print("-------------------------------------------------")
        for index, element in enumerate(data):
            print(str(index) + " -> " + str(element))
        print("-------------------------------------------------")
        print("Max Value = " + str(heapq.getMaxValue(data)))
        print("-------------------------------------------------")
        print("Max Value = " + str(heapq.getMaxByDeletingIt(data)))
        print("---------------")
        print("Max Heap data after picking out the max value :")
        print("------------------------------------------------")
        for index, element in enumerate(data):
            print(str(index) + " -> " + str(element))
    else:
        print("Min Heap data before picking out the min value :")
        print("-------------------------------------------------")
        for index, element in enumerate(data):
            print(str(index) + " -> " + str(element))
        print("-------------------------------------------------")
        print("Min Value = " + str(heapq.getMinValue(data)))
        print("-------------------------------------------------")
        print("Min Value = " + str(heapq.getMinByDeletingIt(data)))
        print("---------------")
        print("Min Heap data after picking out the min value :")
        print("------------------------------------------------")
        for index, element in enumerate(data):
            print(str(index) + " -> " + str(element))

# main function call
main()

