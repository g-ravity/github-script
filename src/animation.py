import threading
import time
import sys


class Animation:
    def __init__(self, text, speed):
        self.text = text
        self.speed = speed

    def start(self):
        self.stop_thread = False
        self.animation_thread = threading.Thread(
            target=self._animate, args=(lambda: self.stop_thread, ))
        self.animation_thread.start()

    def _animate(self, stop):
        self._pattern = '\\|/-'
        self._count = 0

        while True:
            print(self.text, self._pattern[self._count % len(
                self._pattern)], end="\r")
            sys.stdout.flush()
            self._count += 1
            time.sleep(self.speed)
            if stop():
                break

    def stop(self):
        self.stop_thread = True
        self.animation_thread.join()
