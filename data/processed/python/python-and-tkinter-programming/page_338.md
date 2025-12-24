---
source_image: page_338.png
page_number: 338
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.35
tokens: 8162
characters: 1253
timestamp: 2025-12-24T00:40:45.619885
finish_reason: stop
---

CHAPTER 14

Extending Python

14.1 Writing a Python extension 313
14.2 Building Python extensions 316
14.3 Using the Python API in extensions 319
14.4 Building extensions in C++ 320
14.5 Format strings 321
14.6 Reference counts 324
14.7 Embedding Python 325
14.8 Summary 328

Python is readily extensible using a well-defined interface and build scheme. In this chapter, I will show you how to build interfaces to external systems as well as existing extensions. In addition, we will look at maintaining extensions from one Python revision to another. We’ll also discuss the choice between embedding Python within an application or developing a freestanding Python application.

The documentation that comes with Python is a good source of information on this topic, so this chapter will attempt not to repeat this information. My goal is to present the most important points so that you can easily build an interface.

14.1 Writing a Python extension

Many Python programmers will never have a need to extend Python; the available library modules satisfy a wide range of requirements. So, unless there are special requirements, the standard, binary distributions are perfectly adequate.
In some cases, writing an extension in C or C++ may be necessary: