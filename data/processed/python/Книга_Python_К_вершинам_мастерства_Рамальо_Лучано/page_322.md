---
source_image: page_322.png
page_number: 322
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 41.81
tokens: 11763
characters: 1403
timestamp: 2025-12-24T01:49:30.789455
finish_reason: stop
---

Глава 10. Рубим, перемешиваем и нарезаем последовательности

>>> v7.k
Traceback (most recent call last):
    ...
AttributeError: 'Vector' object has no attribute 'k'
>>> v3 = Vector(range(3))
>>> v3.t
Traceback (most recent call last):
    ...
AttributeError: 'Vector' object has no attribute 't'
>>> v3.spam
Traceback (most recent call last):
    ...
AttributeError: 'Vector' object has no attribute 'spam'

Tests of hashing::

>>> v1 = Vector([3, 4])
>>> v2 = Vector([3.1, 4.2])
>>> v3 = Vector([3, 4, 5])
>>> v6 = Vector(range(6))
>>> hash(v1), hash(v3), hash(v6)
(7, 2, 1)

Most hash values of non-integers vary from a 32-bit to 64-bit CPython build::

>>> import sys
>>> hash(v2) == (384307168202284039 if sys.maxsize > 2**32 else 357915986)
True
Tests of ``format()`` with Cartesian coordinates in 2D::
>>> v1 = Vector([3, 4])
>>> format(v1)
'(3.0, 4.0)'
>>> format(v1, '.2f')
'(3.00, 4.00)'
>>> format(v1, '.3e')
'(3.000e+00, 4.000e+00)'

Tests of ``format()`` with Cartesian coordinates in 3D and 7D::

>>> v3 = Vector([3, 4, 5])
>>> format(v3)
'(3.0, 4.0, 5.0)'
>>> format(Vector(range(7)))
'(0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0)'
Tests of ``format()`` with spherical coordinates in 2D, 3D and 4D::
>>> format(Vector([1, 1]), 'h') # doctest:+ELLIPSIS
'<1.414213..., 0.785398...>'
>>> format(Vector([1, 1]), '.3eh')
'<1.414e+00, 7.854e-01>'
>>> format(Vector([1, 1]), '0.5fh')
'<1.41421, 0.78540>'