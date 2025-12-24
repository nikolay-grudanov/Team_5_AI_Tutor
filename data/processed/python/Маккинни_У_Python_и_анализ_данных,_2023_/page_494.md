---
source_image: page_494.png
page_number: 494
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 6.70
tokens: 7178
characters: 554
timestamp: 2025-12-24T02:53:38.173416
finish_reason: stop
---

In [235]: arr_f.copy('C').flags
Out[235]:
    C_CONTIGUOUS : True
    F_CONTIGUOUS : False
    OWNDATA : True
    WRITEABLE : True
    ALIGNED : True
    WRITEBACKIFCOPY : False
    UPDATEIFCOPY : False

При построении представления массива помните, что непрерывность результата не гарантируется:

In [236]: arr_c[:50].flags.contiguous
Out[236]: True

In [237]: arr_c[:, :50].flags
Out[237]:
    C_CONTIGUOUS : False
    F_CONTIGUOUS : False
    OWNDATA : False
    WRITEABLE : True
    ALIGNED : True
    WRITEBACKIFCOPY : False
    UPDATEIFCOPY : False