from log_provider import getLogger

logger = getLogger(__name__)

def is_url_but_not_bitly(url):
    logger.info("sadsad")
    if url.startswith("http://") and not "bit.ly" in url:
        return True
    return False