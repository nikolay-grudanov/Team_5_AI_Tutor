---
source_image: page_381.png
page_number: 381
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.73
tokens: 8328
characters: 2016
timestamp: 2025-12-24T00:42:08.711414
finish_reason: stop
---

You can get similar speedups by caching built-in functions (such as len) or globals (such as other functions defined in the same modules) in local variables.

17.3.6 Using exceptions

The exception mechanism can be a valuable tool to improve performance. Although Python release 1.5.2 has now superseded the following tip by adding new functionality, the principle still applies.

This example looks at using dictionaries. Dictionaries are valuable Python tools since they usually give applications a program boost when there is a need to access data using a key. However, dictionaries used to have a problem: if you tried to access a dictionary entry that did not exist, you got a KeyError. This required programmers to check whether keys existed using:

    if dictionary.has_key(key):
        ...

If the key usually exists, it is generally better to use an exception to trap occasional KeyErrors:

    try:
        value = dictionary[key]
    except KeyError:
        doErrorStuff()

In the current version of Python, you may not need to do any of this; use the get dictionary method:

    value = dictionary.get(key, value_to_use_if_not_defined)

17.3.7 Using map, filter and reduce

Python supports three built-in functions which allow lists to be manipulated. The advantage of using these functions is that you push much of the looping overhead into C code, with an attendant improvement in performance.

map(function, sequence) applies function to each item in the list and returns the resultant values in a new list. Here is a simple example that changes all Y characters to Ks in a list of strings:

    from string import maketrans, translate

    def Y2K(instr):
        return translate(instr, maketrans('yY', 'kK'))

    list = ['thirty', 'Year 2000', 'century', 'yellow']
    print map(Y2K, list)

C:> python map.py
['thirtk', 'Kear 2000', 'centurk', 'kellow']

You can also use map to combine several lists into a list of tuples. Using the previous example:

    print map(None, list, map(Y2K, list))