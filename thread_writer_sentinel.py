import queue
import random
import shelve
import threading
import time
import concurrent.futures

shelf = shelve.open("my.shelf")
items_to_write = queue.Queue()


def writer(sentinel):
    while True:

        item = items_to_write.get()

        if item == sentinel:
            print("Got sentinel, stoping writer thread ...")
            shelf.close()
            return

        key, val = item
        print(f"writing {key}: {val}")
        shelf[str(key)] = val


def write(item):
    items_to_write.put(item)


def producer(url):
    time.sleep(random.random())
    item = (url, f"Dummy data for url {url}")
    write(item)


sentinel = object()

writer_thread = threading.Thread(target=writer, args=(sentinel,))
writer_thread.start()


with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(producer, url) for url in range(5)]

concurrent.futures.wait(futures)

write(sentinel)
