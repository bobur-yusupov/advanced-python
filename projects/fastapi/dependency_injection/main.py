from fastapi import FastAPI, Depends
import time

app = FastAPI()

def expensive_computation(x: int) -> int:
    time.sleep(2)
    return x * x


class Cache:
    def __init__(self):
        self._store = {}

    def get_or_set(self, key: int, compute_func):
        if key not in self._store:
            self._store[key] = compute_func(key)
        
        return self._store[key]
    


cache = Cache()

def get_cache():
    return cache


@app.get("/compute/{x}")
def compute(x: int, cache: Cache = Depends(get_cache)):
    start_time = time.perf_counter()
    result = cache.get_or_set(x, expensive_computation)
    duration = time.perf_counter() - start_time
    return {
        "input": x,
        "result": result,
        "duration": duration
    }
