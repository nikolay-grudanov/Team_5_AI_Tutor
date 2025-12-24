---
source_image: page_165.png
page_number: 165
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.11
tokens: 8195
characters: 1424
timestamp: 2025-12-24T00:35:51.639220
finish_reason: stop
---

CHAPTER 8

Dialogs and forms

8.1 Dialogs 141
8.2 A standard application framework 155
8.3 Data dictionaries 165
8.4 Notebooks 172
8.5 Browsers 175
8.6 Wizards 184
8.7 Image maps 191
8.8 Summary 198

This chapter presents examples of a wide range of designs for dialogs and forms. If you are not in the business of designing and developing forms for data entry, you could possibly expend a lot of extra energy. It’s not that this subject is difficult, but as you will see in “Designing effective graphics applications” on page 338, small errors in design quickly lead to ineffective user interfaces.

The term dialog is reasonably well understood, but form can be interpreted in several ways. In this chapter the term is used to describe any user interface which collects or displays information and which may allow modification of the displayed values. The way the data is formatted depends very much on the type of information being processed. A dialog may be interpreted as a simple form. We will see examples from several application areas; the volume of example code may seem a little overwhelming at first, but it is unlikely that you would ever need to use all of the example types within a single application—pick and choose as appropriate.

We begin with standard dialogs and typical fill-in-the-blank forms. More examples demonstrate ways to produce effective forms without writing a lot of code. The examples will