---
source_image: page_016.png
page_number: 16
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 64.65
tokens: 8414
characters: 2633
timestamp: 2025-12-24T00:32:05.918430
finish_reason: stop
---

preface

I first encountered Python in 1993 when I joined a small company in Rhode Island. Their primary product was a GUI-builder for X/Motif that generated code for C, C++, Ada and Python. I was tasked with extending the object-oriented interface for X/Motif and Python. In the past I’d become skeptical about the use of interpretive languages, so I began the task with little excitement. Two days later I was hooked. It was easy to develop interfaces that would have taken much more time and code to develop in C. Soon after, I began to choose interfaces developed using the Python interface in preference to compiled C code.

After I left the company in Rhode Island, I began to develop applications using Tkinter, which had become the preeminent GUI for Python. I persuaded one company, where I was working on contract, to use Python to build a code-generator to help complete a huge project that was in danger of overrunning time and budget. The project was a success. Four years later there are many Python programmers in that company and some projects now use Tkinter and Python for a considerable part of their code.

It was this experience, though, that led me to start writing this book. Very little documentation was available for Tkinter in the early days. The Tkinter Life Preserver was the first document that helped people pull basic information together. In 1997 Fredrik Lundh released some excellent documentation for the widget classes on the web, and this has served Tkinter programmers well in the past couple of years. One of the problems that I saw was that although there were several example programs available (the Python distribution contains several), they were mostly brief in content and did not represent a framework for a full application written with Tkinter. Of course, it is easy to connect bits of code together to make it do more but when the underlying architecture relies on an interpreter it is easy to produce an inferior product, in terms of execution speed, aesthetics, maintainability and extensibility.

So, one of the first questions that I was asked about writing Tkinter was “How do I make an XXX?” I’d usually hand the person a chunk of code that I’d written and, like most professional programmers, they would work out the details. I believe strongly that learning from full, working examples is an excellent way of learning how to program in a particular language and to achieve particular goals.

When I was training in karate, we frequently traveled to the world headquarters of Shukokai, in New Jersey, to train with the late Sensei Shigeru Kimura. Sensei Kimura often told us “I