# List sebagai stack, Last In First Out (LIFO)
from collections import deque

def main():
    queue = deque(["Andy", "Benny", "Charles"])
    print("Queue: ", queue)
    queue.append("Daniel")
    print("Queue: ", queue)
    queue.append("Erick")
    print("Queue: ", queue)
    queue.popleft()
    print("Queue: ", queue)
    queue.popleft()
    print("Queue: ", queue)

    # Tersedia juga:
    # queue.appendleft("data1")
    # queue.extendleft(["data2", "data3"])
    # print("Queue: ", queue)

if __name__ == "__main__":
    main()

