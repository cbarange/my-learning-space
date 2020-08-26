#!/usr/bin/env python3
# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
from enum import Enum
from threading import Thread, Event


class Status(Enum):
    STOP = "stop"
    START = "start"


class Service(Thread):
    status = Status.START.value
    id = None
    delay = None
    event = None

    def __init__(self, name, delay, event):
        super().__init__()
        self.id = name
        self.delay = delay
        self.event = event

    def run(self):
        while self.status == Status.START.value:
            print(self.id + " is Running...")
            time.sleep(self.delay)
            #self.event.wait(self.delay)

    def stop(self):
        self.status = Status.STOP.value


class Application:
    services = []
    event = Event()

    def __init__(self):
        self.services.append(Service("1", 2, self.event))
        self.services.append(Service("2", 2.5, self.event))
        self.services.append(Service("3", 5, self.event))

    def start(self):
        [service.start() for service in self.services]

    def stop(self):
        [service.stop() for service in self.services]
        self.event.set()
        print(" Stoped !")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = Application()
    try:
        app.start()
        while not input()==Status.STOP.value:
            pass
        app.stop()
    except KeyboardInterrupt:
        app.stop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
