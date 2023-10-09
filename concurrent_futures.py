import concurrent.futures

def f():
    return 1

def g():
    return 2

fa = [f, g]

results = []
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = []
    for ff in fa:
        futures.append(executor.submit(ff))
    for future in concurrent.futures.as_completed(futures):
        results.append(future.result())
    print(max(results))


