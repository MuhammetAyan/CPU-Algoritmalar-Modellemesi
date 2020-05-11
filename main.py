import random
import matplotlib
import numpy

_no = 1
millisecond = 0

proseses = []  # [1, 2, 3]
taskList = []  # (prosesno, time, state) state: ready, waiting


def log(str: str):
    print("[{}] {}".format(millisecond, str))


def Admitted():
    global _no, proseses
    proseses.append(_no)
    taskList.append((_no, random.randint(1, 5), "ready"))
    log(f"Proses admitted P{_no}")
    _no += 1


def Terminated(no: int):
    global proseses
    proseses.remove(no)
    log(f"P{no} terminated!")


def schedulerDispatch():
    global millisecond, ready
    mintime = None
    for prosesno, waitingtime in ready:
        if mintime == None:
            mintime = (prosesno, waitingtime)
        elif int(mintime[1]) > int(waitingtime):
            mintime = (prosesno, waitingtime)
    if mintime != None:
        millisecond += int(mintime[1])
        log("READY Proses no: {}, wait time {}".format(mintime[0], str(mintime[1])))


def olayTara():
    def GetTime(item):
        return item[1]
    global millisecond, taskList
    taskList.sort(key=GetTime, reverse=True)
    prosesNo, time, taskType = taskList.pop()
    if taskType == "ready":
        log(f"Scheduler Dispatch {prosesNo}, {time}ms")
        millisecond += time
    elif taskType == "waiting":
        log(f"")
        millisecond += time
    else:
        pass


while millisecond < 100:
    olayTara()
    if random.randint(0, 1000) == 1:
        Admitted()
