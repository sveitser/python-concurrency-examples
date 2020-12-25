# Concurrency examples

A few examples of using a
[concurrent.futures.ThreadPoolExector](https://docs.python.org/3/library/concurrent.futures.html)
and synchronizing access to resource.

The examples assume we are concurrently fetching data from a list of URLs and
storing the results in a `shelve` as mapping of `URL => Result for URL`.
