---
source_image: page_382.png
page_number: 382
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.14
tokens: 8349
characters: 1891
timestamp: 2025-12-24T00:42:09.120951
finish_reason: stop
---

C:> python map.py
[('thirty', 'thirtk'), ('Year 2000', 'Kear 2000'), ('century', 'centurk'), ('yellow', 'kellow')]

filter(function, sequence) returns a sequence that contains all items for which function returned true. Here is a simple example that selects any item that ends in a seven or is divisible by seven:

def func(n):
    return `n`[-1] == '7' or ( n % 7 == 0 ) # Cocoricos!

print filter(func, range(1,50))

C:> python filter.py
[7, 14, 17, 21, 27, 28, 35, 37, 42, 47, 49]

Finally, reduce(function, sequence) returns a single item constructed by successively applying two items in the sequence as arguments to function. It is very useful as a means of summing a sequence of numbers. We can extend the previous example like this:

...
def sum(n1, n2):
    return n1 + n2

seq = filter(func, range(1,50))
print reduce(sum, seq)

C:> python reduce.py
135

You can even better the performance by replacing the sum function with operator.add. The operator module provides a set of functions, implemented in C, which correspond to the intrinsic Python operators:

import operator
# ....
print reduce(operator.add, seq)

However, it is important to note that map, filter, and reduce are generally slower than inline code when the function is a lambda expression or a function constructed expressly to be used by one of these methods.

17.4 Application profiling

Python has a basic profiling module which allows you to learn where bottlenecks occur in your code. If you do find a point in the code where you spend a lot of time, or execute frequently, you may have a candidate for improvement.

Using the profile module is quite easy and requires minimal changes to your code. Essentially, you have to invoke your application through the profiler. If your application was started by invoking a function start, you would only have to add two lines:

import profile
profile.run('start()')