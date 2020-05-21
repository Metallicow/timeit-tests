# timeit-tests
timeit tests with python/wxPython/etc

![screenie](https://raw.githubusercontent.com/Metallicow/timeit-tests/master/timeit_test_pic.png)


------------------------------------------
```python
        def Test1():
            var0, var1, var2, var3 = [None for i in range(4)]
        def Test2():
            var0, var1, var2, var3 = None, None, None, None
        def Test3():
            var0 = None
            var1 = None
            var2 = None
            var3 = None
```

```
Timeit Test - 100,000,000 times
Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32

Test1:[69.43497820625826, 70.7587834916871, 70.67255975574258]
Test2:[12.67047501201867, 12.61680948817039, 12.617446652853204]
Test3:[14.791721046674354, 14.761109635432547, 14.826768388585037]

Winner: Test2
Loser: Test1
```


