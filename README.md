# timeit-tests
timeit tests with python/wxPython/etc

![screenie](https://raw.githubusercontent.com/Metallicow/timeit-tests/master/timeit_test_pic.png)


------------------------------------------
## Multiple assignment

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

------------------------------------------
## Square root

```python
from math import sqrt

        def Test1():
            a = sqrt(42)
        def Test2():
            a = 42 ** 0.5
```

```
Timeit Test - 1,000,000 times
Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32

Test1:[0.21390546200000005, 0.20380607400000006, 0.2046846379999998, 0.20616916600000001, 0.20404049400000002]
Test2:[0.0977977990000003, 0.0974373420000001, 0.09686914800000013, 0.09571921399999983, 0.09735933799999996]

Winner: Test2
Loser: Test1
```

------------------------------------------
## List comprehension

```python
        def Test1():
            cube_numbers = []
            for n in range(0, 10):
                if n % 2 == 1:
                    cube_numbers.append(n ** 3)
        def Test2():
            cube_numbers = [n ** 3 for n in range(1, 10) if n % 2 == 1]
```

```
Timeit Test - 1,000,000 times
Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:19:08) [MSC v.1500 32 bit (Intel)] on win32

Test1:[1.9607141992067465, 1.9515541358022919, 1.9185960536023]
Test2:[1.4904776312910268, 1.5169179129079637, 1.5596855395228904]

Winner: Test2
Loser: Test1
```

```
Timeit Test - 1,000,000 times
Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32

Test1:[2.434065155999999, 2.440036932, 2.4267266780000014, 2.4286168229999987, 2.443524095000001]
Test2:[2.2794151880000015, 2.289428361999999, 2.2601405449999987, 2.2175954340000033, 2.229053724]

Winner: Test2
Loser: Test1
```

------------------------------------------
## Concatenate strings
In most cases, the 2nd test is cleaner, more elegant, pythonic, and faster despite what the timeit results show. Understand the difference between mutable vs. immutable objects and use your brain to come to a conclusion and avoid controversy.

```python
        def Test1():
            string = "In" + "the" + "face" + "of" + "ambiguity," + "refuse" + "the" + "temptation" + "to" + "guess."
        def Test2():
            string = " ".join(["In", "the", "face", "of", "ambiguity,", "refuse", "the", "temptation", "to", "guess."])
```

```
Timeit Test - 1,000,000 times
Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32

Test1:[0.096437667, 0.09655795599999983, 0.09860985600000038, 0.09880157999999994, 0.0983528549999999]
Test2:[0.4058238170000008, 0.4115426979999999, 0.41353712200000015, 0.4117126640000004, 0.40883433700000005]

Winner: Test1
Loser: Test2
```

------------------------------------------
## Avoiding dots...

```python
        oldlist = ['Python', 'is', 'the', 'best!']
        def Test1():
            newlist = []
            for word in oldlist:
                newlist.append(str.upper(word))
        def Test2():
            newlist = []
            for word in oldlist:
                newlist.append(word.upper())
        def Test3():
            newlist = []
            append = newlist.append
            for word in oldlist:
                append(word.upper())
        def Test4():
            upper = str.upper
            newlist = []
            append = newlist.append
            for word in oldlist:
                append(upper(word))
        def Test5():
            upper = str.upper
            newlist = [upper(word) for word in oldlist]
        def Test6():
            newlist = [word.upper() for word in oldlist]
```

```
Timeit Test - 1,000,000 times
Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:19:08) [MSC v.1500 32 bit (Intel)] on win32

Test1:[1.8504736243791031, 1.8604523130268564, 1.86824649569688]
Test2:[1.490703430630953, 1.4900399911158226, 1.486205097235354]
Test3:[1.3632791154906148, 1.3778066344772597, 1.375073230831381]
Test4:[1.5932545115734467, 1.6161903874347168, 1.6424483874026947]
Test5:[1.4300836976571496, 1.415456005872425, 1.4217028472475661]
Test6:[1.1478029108408734, 1.1512527142107025, 1.1565992320359157]

Winner: Test6
Loser: Test1
```

```
Timeit Test - 1,000,000 times
Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32

Test1:[0.8097238230000006, 0.7958117090000005, 0.7976915919999996, 0.7972740680000001, 0.7990106700000013]
Test2:[0.7080931819999989, 0.7063077249999985, 0.7075434640000005, 0.6980598909999998, 0.6959985480000004]
Test3:[0.6767243170000015, 0.6809196689999979, 0.682192766, 0.6770355100000032, 0.6747935269999985]
Test4:[0.6477554930000018, 0.6499346619999997, 0.6517024649999996, 0.6465616300000008, 0.6448311869999976]
Test5:[0.7440359209999983, 0.7518058819999993, 0.7511325889999974, 0.7383712319999987, 0.7484102700000008]
Test6:[0.6913043859999988, 0.6930968220000011, 0.6919202019999986, 0.683555363, 0.6941917430000011]

Winner: Test4
Loser: Test1
```


