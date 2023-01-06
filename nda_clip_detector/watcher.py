import threading
import pyperclip
import time
from log_provider import getLogger

logger = getLogger(__name__)

class ClipboardWatcher(threading.Thread):
    def __init__(self, predicate, callback, pause=.5):
        super(ClipboardWatcher, self).__init__()
        self._predicate = predicate
        self._callback = callback
        self._pause = pause
        self._stopping = False

    def run(self):
        logger.debug("Start watching...")
        recent_value = ""
        while not self._stopping:
            tmp = pyperclip.paste()
            if tmp != recent_value:
                recent_value = tmp
                if self._predicate(recent_value):
                    self._callback(recent_value)
            time.sleep(self._pause)

    def stop(self):
        logger.debug("Stop watching...")
        self._stopping = True