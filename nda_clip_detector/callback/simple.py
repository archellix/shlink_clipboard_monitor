import pyperclip
from log_provider import getLogger

logger = getLogger(__name__)

def print_to_stdout(clipboard_content):
    pyperclip.copy("111")
    logger.debug("Found url: %s" % str(clipboard_content))
