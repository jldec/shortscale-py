import shortscale
import timeit

NUM = 740_991_777

store = []

def setup():
  store.clear()

def run():
  store.append(shortscale.shortscale(NUM))

def report(calls:int, time:float):
  print(f'{calls:10d} calls, {calls * 100:10d} bytes, {time * 1_000_000_000 / calls:>8.0f} ns/call')

t = timeit.Timer('shortscale.shortscale(NUM)', 'pass', globals=globals())

t.autorange(report)
