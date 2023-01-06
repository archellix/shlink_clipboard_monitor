import time

from bestconfig import Config

from log_provider import getLogger
from watcher import ClipboardWatcher
from predicate.simple import is_url_but_not_bitly
from callback.simple import print_to_stdout

config = Config()
logger = getLogger(__name__)

def app():
    watcher = ClipboardWatcher(is_url_but_not_bitly, print_to_stdout, 5.)
    
    watcher.start()
    while True:
        try:
            logger.debug("Waiting for changed clipboard...")
            time.sleep(config['system'].float('scan_interval'))
        except KeyboardInterrupt:
            watcher.stop()
            break;

if __name__ == "__main__":
    app()