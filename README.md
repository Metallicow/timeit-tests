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
This testcase involves a common operation UPPERCASE/lowercase, and explores numerous ways to write it.

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
        def Test7():
            newlist = map(str.upper, oldlist)
```

```
Timeit Test - 1,000,000 times
Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:19:08) [MSC v.1500 32 bit (Intel)] on win32

Test1:[1.8817726972470135, 1.8519277721282326, 1.846382961428136]
Test2:[1.4698498352280636, 1.4924597389513297, 1.5008184199711732]
Test3:[1.3935009202349455, 1.3827475345791171, 1.3910590030096994]
Test4:[1.6171161647284187, 1.6034462726892418, 1.609554350106393]
Test5:[1.396877236183233, 1.4140843775184315, 1.40762897966205]
Test6:[1.1577150913194103, 1.1546442202964045, 1.1550974611532752]
Test7:[1.3996742741885484, 1.3997900476682936, 1.4010606821357001]

Winner: Test6
Loser: Test1
```

```
Timeit Test - 1,000,000 times
Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32

Test1:[0.780131382, 0.7885405600000004, 0.7914447500000001, 0.7931054020000001, 0.7907677629999998]
Test2:[0.7016365530000002, 0.690991962, 0.6978817150000003, 0.709509559999999, 0.7045497750000003]
Test3:[0.6750850129999986, 0.6738184839999999, 0.6853946009999987, 0.6747483680000013, 0.6721311480000001]
Test4:[0.6532641760000004, 0.6480859809999995, 0.6498119090000003, 0.6482842739999999, 0.6490392650000008]
Test5:[0.7435810379999985, 0.7422558009999989, 0.7406518049999988, 0.725172643999997, 0.7178674189999974]
Test6:[0.6611761849999986, 0.6739092140000018, 0.6893711320000016, 0.6897090099999978, 0.6886337950000012]
Test7:[0.28037093400000046, 0.28517266000000063, 0.28431667599999955, 0.28404243200000323, 0.282711857999999]

Winner: Test7
Loser: Test1
```

------------------------------------------
## Formatting

```python
        def Test1():
            var = '!'
            msg = 'Hello ' + var + ' World'
        def Test2():
            var = '!'
            msg = 'Hello %s World' % var
        def Test3():
            var = '!'
            msg = 'Hello {} World'.format(var)
        def Test4():
            var = '!'
            msg = f'Hello {var} World'
```

```
Timeit Test - 1,000,000 times
Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32

Test1:[0.21141304800000027, 0.21259952100000046, 0.2115025459999993, 0.21131000200000027, 0.21373180199999986]
Test2:[0.28735429199999984, 0.28459420400000024, 0.2868669759999998, 0.2853984600000006, 0.2904526700000005]
Test3:[0.39456012499999993, 0.40041202200000026, 0.39395251899999995, 0.3969847980000001, 0.40249060699999983]
Test4:[0.18934506299999931, 0.19415171500000028, 0.19184158200000034, 0.19289339600000055, 0.18939391699999852]

Winner: Test4
Loser: Test3
```

------------------------------------------
## wx.Point() creation

```python
        def Test1():
            border_points = [wx.Point(0, 0), wx.Point(0, 0), wx.Point(0, 0), wx.Point(0, 0), wx.Point(0, 0), wx.Point(0, 0)]
        def Test2():
            border_points = [wx.Point(), wx.Point(), wx.Point(), wx.Point(), wx.Point(), wx.Point()]
        def Test3():
            border_points = [wx.Point() for i in range(6)]
        def Test4():
            border_points = [wx.Point() for i in xrange(6)]
        def Test5():
            wxPoint = wx.Point
            border_points = [wxPoint() for i in range(6)]
        def Test6():
            wxPoint = wx.Point
            border_points = [wxPoint() for i in xrange(6)]
```

```
Timeit Test - 1,000,000 times
Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:19:08) [MSC v.1500 32 bit (Intel)] on win32
wxPython 4.0.7.post2 msw (phoenix) wxWidgets 3.0.5

Test1:[5.072260522965598, 5.107448809219329, 5.075535369948506]
Test2:[3.048939195078164, 3.035480588002738, 3.011435895393742]
Test3:[3.6908186460599417, 3.6909738287300584, 3.6717032611761304]
Test4:[3.6099861279830137, 3.686791696823967, 3.589700715030837]
Test5:[3.4245194366294314, 3.432768339779436, 3.4454243486535816]
Test6:[3.3247501169001694, 3.3719995451259237, 3.3495813968000334]

Winner: Test2
Loser: Test1
```

```
Timeit Test - 1,000,000 times
Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
wxPython 4.0.7.post2 msw (phoenix) wxWidgets 3.0.5

Test1:[5.187449170000001, 5.094413465000001, 5.132956241999999, 5.174223747999999, 5.118955317000001]
Test2:[3.947080655999997, 3.9596147369999954, 3.9694856679999972, 4.0114383579999995, 4.041925595000002]
Test3:[4.553662209000002, 4.6194235329999955, 4.5218846560000046, 4.600061825999994, 4.536709117000001]
Test5:[4.458740910000003, 4.4787163679999935, 4.378479858999995, 4.373799335000001, 4.382705096999999]

Winner: Test2
Loser: Test1
```

