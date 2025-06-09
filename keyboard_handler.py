import sys
from multiprocessing import Queue
from multiprocessing import Process


class KeyboardHandler:
    def __init__(self):
        self.queue = Queue()

    def get_input_available(self):
        return self.queue.qsize() != 0

    def get_input(self) -> str:
        return self.queue.get()

    def start(self):
        self.process = Process(target=self._monitor_keyboard)
        self.process.daemon = True
        self.process.start()

    def stop(self):
        self.process.terminate()

    def _monitor_keyboard(self):
        sys.stdin = open(0)
        while True:
            self.queue.put(sys.stdin.readline().strip())
