---
source_image: page_031.png
page_number: 31
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.88
tokens: 8248
characters: 998
timestamp: 2025-12-24T00:32:13.626113
finish_reason: stop
---

Concatenating lists
Combining lists works well:

    lst = [1, 2, 3] + [4, 5, 6]
    print lst
    [1, 2, 3, 4, 5, 6]

Iterating through members
Iterating through a list is easy:

    lst = ['first', 'second', 'third']
    for str in lst:
        print 'this entry is %s' % str

    set = [(1, 'uno'), (2, 'due'), (3, 'tres')]
    for integer, str in set:
        print 'Numero "%d" in Italiano: è "%s"' % (integer, str)

Sorting and reversing
Lists have built-in sort and reverse methods:

    lst = [4, 5, 1, 9, 2]
    lst.sort()
    print lst
    [1, 2, 4, 5, 9]

    lst.reverse()
    print lst
    [9, 5, 4, 2, 1]

Indexing
Finding an entry in a list:

    lst = [1, 2, 4, 5, 9]
    print lst.index(5)
    3

Member
Checking membership of a list is convenient:

    if 'jeg' in ['abc', 'tuv', 'kie', 'jeg']:
        ...
    if '*' in '123*abc':
        ...

Modifying members
A list member may be modified in place:

    lst = [1, 2, 4, 5, 9]
    lst[3] = 10
    print lst
    [1, 2, 4, 10, 9]