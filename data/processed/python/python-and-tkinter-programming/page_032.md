---
source_image: page_032.png
page_number: 32
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.37
tokens: 8315
characters: 1392
timestamp: 2025-12-24T00:32:17.228956
finish_reason: stop
---

Inserting and deleting members

To insert a member in a list:

    lst = [1, 2, 3, 4, 10, 9]
    lst.insert(4, 5)
    print lst
    [1, 2, 3, 4, 5, 10, 9]

To delete a member:

    lst = [1, 2, 3, 4, 10, 9]
    del lst(4)
    print lst
    [1, 2, 3, 4, 9]

1.2.2 Tuples

Tuples are similar to lists but they are immutable (meaning they cannot be modified). Tuples are a convenient way of collecting data that may be passed as a single entity or stored in a list or dictionary; the entity is then unpacked when needed.

Initializing tuples
With the exception of a tuple containing one element, tuples are initialized in a similar manner to lists (lists and tuples are really related sequence types and are readily interchangeable).

    tpl = ()                        # Empty tuple
    tpl = (1,)                       # Singleton tuple
    tpl = ('a', 'b', 'c')            # String tuple
    tpl = (1, 2, 3, 4)               # Integer tuple
    tpl = ([1,2,3], ['a','b','c'])   # Tuple of lists
    tpl = ((1,'a'),(2,'b'),(3,'c'))  # Tuple of tuples

Iterating through members

    for i in tpl:
        ...
    for i,a in ((1, 'a'), (2, 'b'), (3, 'c')):
        ...

Modifying tuples
(But you said tuples were immutable!)

    a = 1, 2, 3
    a = a[0], a[1], 10, a[2]
    a
    (1, 2, 10, 3)

Note that you are not modifying the original tuple but you are creating a new name binding for a.