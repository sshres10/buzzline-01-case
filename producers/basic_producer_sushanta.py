import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def generate_messages():
    messages = [
        "Arsenal FC: Arteta praises team's performance.",
        "Arsenal FC: Saka scores a stunning goal!",
        "Arsenal FC: New signing announced.",
        "Arsenal FC: Training updates ahead of the weekend.",
        "Arsenal FC: Fans celebrate a big win.",
    ]
    for message in messages:
        yield message
        time.sleep(1)

if __name__ == "__main__":
    logger.info("Starting producer...")
    for message in generate_messages():
        logger.info(message)
