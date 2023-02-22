# shortscale

[![CI](https://github.com/jldec/shortscale-py/workflows/CI/badge.svg)](https://github.com/jldec/shortscale-py/actions)  

Python module to convert integers into English words.

This is the Python port of the shortscale function, originally written in [JavaScript](https://github.com/jldec/shortscale) and [Rust](https://github.com/jldec/shortscale-rs), documented [here](https://jldec.me/forays-from-node-to-rust). There is a also a [Go](https://github.com/jldec/shortscale-go) version.

The [short scale](https://en.wikipedia.org/wiki/Long_and_short_scales#Comparison), has different words for each power of 1000.

This implementation expresses positive and negative numbers from zero to thousands, millions, billions, trillions, quadrillions etc, up to 10**33 - 1.

### Function
```python
def shortscale(num: int) -> str
```

### Example
```python
import shortscale

// ==> four hundred and twenty billion nine hundred and ninety nine thousand and fifteen
print(shortscale.shortscale(420_000_999_015))
```

After installing this module, the function can also be called from the commnd line e.g.

```sh
$ shortscale 420_000_999_015
420,000,999,015 => four hundred and twenty billion nine hundred and ninety nine thousand and fifteen

$ shortscale 0xffffffff
4,294,967,295 => four billion two hundred and ninety four million nine hundred and sixty seven thousand two hundred and ninety five
```

### Benchmarks
```sh
$ pip install -e .
$ python tests/bench_shortscale.py 
         1 calls,        100 bytes,    11000 ns/call
         2 calls,        200 bytes,     5730 ns/call
         5 calls,        500 bytes,     4625 ns/call
        10 calls,       1000 bytes,     4283 ns/call
        20 calls,       2000 bytes,     4319 ns/call
        50 calls,       5000 bytes,     4169 ns/call
       100 calls,      10000 bytes,     4349 ns/call
       200 calls,      20000 bytes,     4129 ns/call
       500 calls,      50000 bytes,     4021 ns/call
      1000 calls,     100000 bytes,     3943 ns/call
      2000 calls,     200000 bytes,     3484 ns/call
      5000 calls,     500000 bytes,     3097 ns/call
     10000 calls,    1000000 bytes,     2522 ns/call
     20000 calls,    2000000 bytes,     2180 ns/call
     50000 calls,    5000000 bytes,     2112 ns/call
    100000 calls,   10000000 bytes,     2117 ns/call
```

### Test
```sh
$ pip install pytest
$ pip install -e .
$ pytest
============================= test session starts ==============================
platform darwin -- Python 3.10.9, pytest-7.2.1, pluggy-1.0.0
rootdir: /Users/jldec/pub/shortscale-py
collected 1 item                                                               

tests/test_shortscale.py .                                               [100%]

============================== 1 passed in 0.00s ===============================
```

### Build
This assumes that access to pypi.org has been configured 

```sh
pip install build twine
python -m build
python -m twine upload dist/*
````
