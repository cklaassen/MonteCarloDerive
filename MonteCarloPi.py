import random
import numpy
import matplotlib.pyplot as plt
from threading import Thread
from queue import Queue

timesToRun = 2000000
numOfThreads = 64
pointsInCircle = 0
itemsRan = 0

def initiate():
    q = Queue(maxsize=0)
    for i in range(1, timesToRun + 1):
        q.put(i)
    for i in range(numOfThreads):
        print("Starting Thread" + str(i))
        worker = Thread(target=main, args=[q,])
        worker.setDaemon(True)
        worker.start()
    q.join()



timeList = []
piList = []

def main(q):
    global pointsInCircle
    while not q.empty():
        toDo = q.get()
        q.task_done()
        print(toDo)
        if numpy.sqrt(random.uniform(-1, 1) ** 2 + random.uniform(-1, 1) ** 2) <= 1:
            pointsInCircle = pointsInCircle + 1
            if toDo % 10000 == 0:
                pi = (pointsInCircle / toDo) * 4
                timeList.append(toDo)
                piList.append(pi)
    return True

def getMath():
    print((pointsInCircle / timesToRun) * 4)
    plt.scatter(timeList, piList, color='green')
    plt.show()

initiate()
getMath()