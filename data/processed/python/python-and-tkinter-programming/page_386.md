---
source_image: page_386.png
page_number: 386
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 11.50
tokens: 8113
characters: 1181
timestamp: 2025-12-24T00:41:58.027004
finish_reason: stop
---

CHAPTER 18

Threads and asynchronous techniques

18.1 Threading  361
18.2 “after” processing  369
18.3 Summary  373

Applications frequently have a need to process actions as parallel tasks or to perform time-consuming operations. This chapter covers threads and other techniques that support background processing. This area of programming for Python and Tkinter poses special problems that must be solved to prevent system hangs and unexpected behavior. It is also a difficult area to debug, since problems usually occur when the system is running at full speed, outside of any debugger or without debug print statements.

18.1 Threading

Threads provide a means to allow multiple tasks, or threads, to share a global data space. Sometimes they are referred to as lightweight processes, but I think that can be a little misleading; if you regard threads as subprocesses of the same process, it might be easier to understand how they are related.

Python provides two threading interfaces. The thread module provides low-level primitives to facilities to control and synchronize threads. The threading module is a higher-level interface which is built on top of the thread module.