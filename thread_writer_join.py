import queue
import random
import shelve
import threading
import time
from concurrent.futures import ThreadPoolExecutor

shelf = shelve.open("my.shelf")
items_to_write = queue.Queue()


def writer():
    while True:
        item = items_to_write.get()
        key, val = item
        print(f"writing {key}: {val}")

        # shelf only supports string keys
        shelf[str(key)] = val

        items_to_write.task_done()


def queue_for_writing(item):
    items_to_write.put(item)


def producer(url):
    time.sleep(random.random())
    # do some actual work here
    item = (url, f"Dummy data for url: {url}")
    queue_for_writing(item)


# Without daemon=True the program doesn't exit.
writer_thread = threading.Thread(target=writer, daemon=True)
writer_thread.start()

with ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(producer, range(5))

# If no item is put on the queue yet, will it exit right at the start?
items_to_write.join()

shelf.close()
