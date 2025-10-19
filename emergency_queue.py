
class Patient:
    def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency

    def __repr__(self):
        return f"{self.name} ({self.urgency})"


class MinHeap:
    def __init__(self):
        self.data = []

    def insert(self, patient):
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    def heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.data[index].urgency < self.data[parent].urgency:
                self.data[index], self.data[parent] = self.data[parent], self.data[index]
                index = parent
            else:
                break

    def heapify_down(self, index):
        size = len(self.data)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < size and self.data[left].urgency < self.data[smallest].urgency:
                smallest = left
            if right < size and self.data[right].urgency < self.data[smallest].urgency:
                smallest = right

            if smallest != index:
                self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
                index = smallest
            else:
                break

    def peek(self):
        return self.data[0] if self.data else None

    def remove_min(self):
        if not self.data:
            return None
        if len(self.data) == 1:
            return self.data.pop()

        root = self.data[0]
        self.data[0] = self.data.pop()
        self.heapify_down(0)
        return root

    def print_heap(self):
        print("Current Queue:")
        for patient in self.data:
            print(f"- {patient.name} ({patient.urgency})")


#Test
if __name__ == "__main__":
    heap = MinHeap()
    heap.insert(Patient("Jordan", 3))
    heap.insert(Patient("Taylor", 1))
    heap.insert(Patient("Avery", 5))
    heap.print_heap()
    # Expected:
    # Current Queue:
    # - Taylor (1)
    # - Jordan (3)
    # - Avery (5)

    next_up = heap.peek()
    print(next_up.name, next_up.urgency)  # Taylor 1

    served = heap.remove_min()
    print(served.name)  # Taylor
    heap.print_heap()
    # Expected:
    # Current Queue:
    # - Jordan (3)
    # - Avery (5)
