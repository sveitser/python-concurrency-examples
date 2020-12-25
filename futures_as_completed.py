import random
import shelve
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

shelf = shelve.open("my.shelf")


def producer(url):
    time.sleep(0.1 * random.random())
    item = (url, f"Dummy data for url {url}")
    return item


with ThreadPoolExecutor(max_workers=5) as executor:

    futures = [executor.submit(producer, url) for url in range(5)]

    for fut in as_completed(futures):
        key, val = fut.result()
        print(f"Writing {key}: {val}")
        shelf[str(key)] = val


shelf.close()
