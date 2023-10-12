import os
import threading
from src.yaaylibs import yaay_splash
from src.yaaylibs.message_broker_setup import import_message_handlers, setup_broker_queues


if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.abspath(__file__))
    yaay_splash.yaay_splash()
    imported_classes = import_message_handlers(script_dir)
    workers = setup_broker_queues(imported_classes, script_dir)
    threads = [threading.Thread(target=worker.start_consuming) for worker in workers]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
